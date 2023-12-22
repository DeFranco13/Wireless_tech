export default function Data({ data:data }){
    return (
        <table>
            <tbody>
            <tr>
                <th className="text-left">SSID</th>
                <th className="text-left">MODE</th>
                <th className="text-left">SECURITY</th>
                <th className="text-left">RATE</th>
                <th className="text-left">SIGNAL</th>
                <th className="text-left">CHAN</th>
                
            </tr>
                {data?.map((s, i) => 
                <tr key={i}>
                    <td>{s.SSID}</td>
                    <td>{s.MODE}</td>
                    <td>{s.SECURITY}</td>
                    <td>{s.RATE}</td>
                    <td>{s.SIGNAL}</td>
                    <td>{s.CHAN}</td>
                </tr>)}
            </tbody>
        </table>

    )
}