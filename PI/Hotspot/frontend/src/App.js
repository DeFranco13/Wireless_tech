import axios from "axios";
import { useEffect, useState } from "react";
import Data from "./Data";
import Chart from "./Chart";

function App() {
  const [scans, setScans] = useState([]);
  useEffect(() => {
        // axios.get("http://localhost:8080/").then((r) => setScans(r.data)).catch((e) => console.log(e));   
        console.log(window.location.href)
        let url = new URL("/ws", window.location.href)
        url.port = "8080";
        url.protocol = url.protocol.replace("http","ws");
        console.log(url.href);

        let ws = new WebSocket(url.href);
        ws.onmessage = (m) => {
          const msg = JSON.parse(m.data);
          console.log(msg);
          if (Array.isArray(msg)){
            setScans((p) => [...p, ...msg]);
          } else {
            setScans((p) => [...p, msg]);
          }
        }
  }, []);

  return (
    <div className="flex flex-col">
        <Chart scans={scans}/>
        <div>{scans.length} wifi netwerken gescand</div>
        <Data data={scans} />
    </div>
  );
} 

export default App;
