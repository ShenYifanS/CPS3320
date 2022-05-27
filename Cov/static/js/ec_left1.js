var ec_left1 = echarts.init(document.getElementById('l1'), "dark");
var ec_left1_Option = {
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['New diagnosis', 'New suspected'],
		left: "right"
	},
	//title style
	title: {
		text: "New Local trends",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	//Graphic location
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		//The start and end points of the x-axis coordinate points are not at the edge
		// boundaryGap : true,

		data: []
	}],
	yAxis: [{
		type: 'value',
		//y-axis font settings
		//y-axis setting display
		axisLine: {
			show: true
		},
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				// color: '#FFF',
				width: 1,
				// type: 'solid',
			}
		}
	}],
	series: [{
		name: "New diagnosis",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "New suspected",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left1.setOption(ec_left1_Option)
