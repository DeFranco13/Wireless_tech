use std::sync::{Arc, Mutex};

use axum::extract::ws::WebSocket;
use axum::extract::{State, WebSocketUpgrade};
use axum::http::Method;
use axum::response::IntoResponse;
use axum::{Router, Json};
use axum::routing::{post, get};
use serde::{Deserialize, Serialize};
use tokio::sync::broadcast::{Sender, Receiver};
use tower_http::cors::{CorsLayer, Any};
use axum::extract::ws::Message;


#[derive(Debug, Deserialize, Serialize,Clone)]
#[serde(rename_all="UPPERCASE")]
pub struct ScanResult {
    ssid: String,
    mode: String,
    chan: u32,
    rate: u32,
    signal: u32,
    security: String
}

#[derive(Debug, Clone)]
pub struct AppState{
    db: Arc<Mutex<Vec<ScanResult>>>,
    tx: Sender<ScanResult>
}


#[tokio::main]
async fn main() {
    let (tx, _) = tokio::sync::broadcast::channel::<ScanResult>(1);
    let appstate = AppState {
        db: Arc::new(Mutex::new(Vec::new())),
        tx
    };

    let cors = CorsLayer::new()
    .allow_methods([Method::GET, Method::POST])
    .allow_origin(Any);


    let app = Router::new()
        .route("/", post(upload))
        .route("/ws", get(ws))
        .layer(cors)
        .with_state(appstate);

    // run our app with hyper, listening globally on port 3000
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn upload(State(s): State<AppState>, Json(scan) : Json<ScanResult>)
{
    let mut db = s.db.lock().unwrap();
    db.push(scan.clone());
    println!("{:?}", scan);
    let _ = s.tx.send(scan);

}

async fn ws(ws: WebSocketUpgrade, State(s): State<AppState>) -> impl IntoResponse {
    ws.on_upgrade(|ws| async move { ws_handler(ws, s).await })
}

async fn ws_handler(mut socket: WebSocket, s: AppState ){
    let scans;
    {
        let db = s.db.lock().unwrap();
        scans = db.clone();
    }

    let _ = socket.send(
        Message::Text( serde_json::to_string(&scans).unwrap())
        ).await;

    let mut rx = s.tx.subscribe();
    while let Ok(data) = rx.recv().await {
        let _ = socket.send(Message::Text(
                serde_json::to_string(&data).unwrap()
                )).await;
    }
}
