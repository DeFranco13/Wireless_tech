use std::sync::{Arc, Mutex};

use axum::extract::State;
use axum::{Router, Json};
use axum::routing::post;
use serde::{Deserialize, Serialize};


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

#[derive(Clone, Debug)]
pub struct DB (Arc<Mutex<Vec<ScanResult>>>);

#[tokio::main]
async fn main() {
    let db = DB(Arc::new(Mutex::new(Vec::new())));


    let app = Router::new()
        .route("/", post(upload).get(fetch))
        .with_state(db);

    // run our app with hyper, listening globally on port 3000
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn upload(State(db): State<DB>, Json(scan) : Json<ScanResult>) -> String
{
    println!("{:?}", scan);
    let mut db = db.0.lock().unwrap();
    db.push(scan);
    String::from("HELLO")
}

async fn fetch(State(db): State<DB>) -> Json<Vec<ScanResult>>
{
    let db = db.0.lock().unwrap().clone();
    Json(db)
}
