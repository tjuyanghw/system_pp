    var data =eval('{{ name|safe }}');
    console.log(data);
    for( var i=0;i<data.length;i++){
        var review = data[i].review;
        var label_data = data[i].label;
            if(label_data==0){
				var a0 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a0.style("color","white")
			}
			if(label_data==1){
				var a1 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a1.style("color","purple")
			}
			if(label_data==2){
				var a2 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a2.style("color","pink")
			}
			if(label_data==3){
				var a3 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a3.style("color","green")
			}

			if(label_data==4){
				var a4 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a4.style("color","yellow")
			}
			if(label_data==5){
				var a5 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a5.style("color","orange")
			}
			if(label_data==6){
				var a6 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a6.style("color","blue")
			}
			if(label_data==7){
				var a7 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a7.style("color","#afdfe4")
			}
			if(label_data==8){
				var a8 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a8.style("color","#66AFB2")
			}
			if(label_data==9){
				var a9 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a9.style("color","#D3D1C5")
			}
			if(label_data==10){
				var a10 = d3.select("div.chart").append("p").selectAll("p").data(review).enter().append("text").text(function(d){return d;});
				a10.style("color","#79CED7")
			}
    }




     var obj = {}, k, arr1 = [];
        for (var i = 0, len = data.length; i < len; i++) {
            k = data[i].label;
            if (obj[k])
                obj[k]++;
            else
                obj[k] = 1;
        }
        console.log(obj)
        //保存结果{0-'元素'，count-出现次数}
        for (var o in obj) {
            arr1.push([o, obj[o]
            ]);
        }
        console.log(arr1);



        var pie = d3.layout.pie().value(function (d) {
            return d[1];
        });
        var piedata = pie(arr1);
        console.log(piedata)
        var width = 390;
        var height = 350;
        var svg = d3.select("div.label").append("svg").attr("width", width).attr("height", height);
        var outerRadius = width / 3;           // 外半径
        var innerRadius = 0;             // 内半径
        var arc = d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius);
        var color = d3.scale.category10();
        var arcs = svg.selectAll("g").data(piedata).enter().append("g").attr("transform", "translate(" + (width / 2.5) + "," + (height / 2.5) + ")");
        arcs.append("path").attr("fill", function (d, i) {
            return color(i);
        }).attr("d", function (d) {
            return arc(d);
        });
        arcs.append("text").attr("transform", function (d) {
            var x = arc.centroid(d)[0] * 1.4;
            var y = arc.centroid(d)[1] * 1.4;
            return "translate(" + x + "," + y + ")";
            // return "translate(" + arc.centroid(d)[0] + ")";
        }).attr('text-anchor', 'middle').text(function (d) {
            return d.data[1];
        });
        var tooltip = d3.select("div.label").append("div").attr("class", "tooltip").attr("opacity", 0.0);

        arcs.on("mouseover", function (d, i) {
            console.log(d.data[0] + "标签的数量为" + "<br />" + d.data[1])
            tooltip.html(d.data[0] + "标签的数量为" + "<br />" + d.data[1])
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY + 20) + "px")
                .style("opacity", 1.0);
            tooltip.style("box-shadow", "10px 0px 0px" + color(i));
        })
            .on("mousemover", function (d) {
                tooltip.style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY + 1) + "px");
            })
            .on("mouseout", function (d) {

                tooltip.style("opacity", 0.0);
            });