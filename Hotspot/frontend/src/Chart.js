import {XYPlot, XAxis, YAxis, HorizontalGridLines, LineSeries, BarSeries, VerticalGridLines, LabelSeries, VerticalBarSeries} from 'react-vis';
import '../node_modules/react-vis/dist/style.css';



export default function Chart({ scans:scans }){

    if (scans?.length == 0){
        return <div>niks</div>
    }

    const wpa3 = scans.filter((d) => d.SECURITY.includes("WPA3"));
    const wpa2 = scans.filter((d) => d.SECURITY.includes("WPA2"));
    const wpa1 = scans.filter((d) => d.SECURITY.includes("WPA1"));

    const channels = [...new Set(scans.map((d)=> d.CHAN))].sort();
    const chan_data = channels.map((c)=> ({ x: `chan${c}`, y: scans.filter((d)=> d.CHAN == c).length}));

    const sec_data = [{x: "WPA1", y: wpa1.length}, {x: "WPA2", y: wpa2.length},{x: "WPA3", y: wpa3.length}];

    const rates = [...new Set(scans.map((d)=> d.RATE))].sort();
    const rates_data = rates.map((r)=> ({ x: r, y: scans.filter((d)=> d.RATE == r).length}));

    const signal = [...new Set(scans.map((d)=> d.SIGNAL))].sort();
    const signal_data = signal.map((r)=> ({ x: r, y: scans.filter((d)=> d.SIGNAL == r).length}));
    // console.log(signal_data);

    // console.log(scans)
    return(
        <>
        <div className='flex flex-row'>
        <XYPlot xType="ordinal" width={200} height={300} xDistance={100}>
        <VerticalGridLines />
        <HorizontalGridLines />
        <XAxis />
        <YAxis />
        <VerticalBarSeries data={sec_data} />
    </XYPlot>
    <XYPlot xType="ordinal" width={700} height={300} xDistance={100}>
        <VerticalGridLines />
        <HorizontalGridLines />
        <XAxis title='Channels'/>
        <YAxis />
        <VerticalBarSeries data={chan_data} />
    </XYPlot>
        </div>
        <div className='flex flex-row'>
        <XYPlot margin={50} width={400} height={400}>
      <VerticalGridLines />
      <XAxis title='Rates'/>
      <YAxis />
      <LineSeries data={rates_data} />
    </XYPlot>

    <XYPlot margin={50} xType="linear" width={400} height={400}>
    <VerticalGridLines />
      <XAxis title='Signals' />
      <YAxis />
      <LineSeries data={signal_data} />
    </XYPlot>
        </div>
    </>
  )
}