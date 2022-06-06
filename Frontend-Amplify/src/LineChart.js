import CanvasJSReact from './canvasjs/canvasjs.react';
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

function LineChart(props) {

    const options = {
        animationEnabled: true,
        exportEnabled: true,
        theme: "dark1", // "light1", "dark1", "dark2"
        title:{
            text: "Bitcoin Price Prediction for Next 12 Hours"
        },
        axisY: {
            title: "Price",
            prefix: "$"
        },
        axisX: {
            title: "Hour",
            interval: 1
        },
        data: [{
            type: "line",
            toolTipContent: "Hour {x}: ${y}",
            dataPoints: [
                { x: 1, y: props.prices[0] },
                { x: 2, y: props.prices[1] },
                { x: 3, y: props.prices[2] },
                { x: 4, y: props.prices[3] },
                { x: 5, y: props.prices[4] },
                { x: 6, y: props.prices[5] },
                { x: 7, y: props.prices[6] },
                { x: 8, y: props.prices[7] },
                { x: 9, y: props.prices[8] },
                { x: 10, y: props.prices[9] },
                { x: 11, y: props.prices[10] },
                { x: 12, y: props.prices[11] },
            ]
        }]}

    return (
    <div>
        <CanvasJSChart options = {options}
            /* onRef={ref => this.chart = ref} */
        />
        {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
    </div>
    );
}
export default LineChart;                              