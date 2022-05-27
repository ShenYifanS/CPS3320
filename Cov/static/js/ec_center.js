var ec_center = echarts.init(document.getElementById('c2'), "dark");

var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]

var ec_center_option = {
    title: {
        text: 'Confirmed cases nationwide',
        subtext: '',
        x: 'left'
    },

    tooltip: {
        trigger: 'item'
    },
    //Small navigation icon on the left
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 1,end: 9 },
            {start: 10, end: 99 }, 
			{ start: 100, end: 999 },
            {  start: 1000, end: 9999 },
            { start: 10000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //configuration properties
    series: [{
        name: 'Number of confirmed',
        type: 'map',
        mapType: 'china',
        roam: false, //Drag and zoom
        itemStyle: {
            normal: {
                borderWidth: .5, //area border width
                borderColor: '#62d3ff', //area border color
                areaColor: "#b7ffe6", //area color
            },
            emphasis: { //Mouse over the map highlighting related settings
                borderWidth: .5,
                borderColor: '#fff',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //province name
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data:[] //mydata
    }]
};
ec_center.setOption(ec_center_option)