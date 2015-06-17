
 <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
        var json_data = <?php echo $this->register->clientstats; ?> 
    
        var platformstats = [['platformstats','pageviews'],];
        var browserstats = [['browserstats','pageviews'],];

        if(json_data['returndata']){
            json_data = json_data['returndata'];
            var count = 0
            for (key in json_data) {

                var forname = Object.keys(json_data)[count]

                for(var x in json_data[forname]){
                    var forsub = forname.substring(0, 6)
                    console.log('platfo=='+forsub)

                    try {
                            if(forsub == 'platfo'){
                                var ps_platform = json_data[forname][x]['platform']
                            }else if (forsub == 'browse') {
                                var bs_browser = json_data[forname][x]['browser']
                            } 
                        }
                        catch(err) {
                            if(forsub == 'platfo'){
                                var ps_platform = 'no platform'
                            }else if (forsub == 'browse') {
                                var bs_browser = 'no browser'
                            } 
                        } 
                        try {
                            if(forsub == 'platfo'){
                                var ps_pageviews = json_data[forname][x]['pageviews']
                            }else if (forsub == 'browse') {
                                var bs_pageviews = json_data[forname][x]['pageviews']
                            } 
                        }
                        catch(err) {
                            var ps_pageviews = '0'
                        }

                        if(forsub == 'platfo'){
                            platformstats.push([ps_platform,ps_pageviews])
                        }else if (forsub == 'browse') {
                             browserstats.push([bs_browser,bs_pageviews])
                        }
                    }
                    count++;
                }
            }

        var tableArray = [browserstats,platformstats]

        google.load("visualization", "1", {packages:["geochart","table","corechart"]});
        var cssClasses = {headerRow: 'tblHeaderClass',hoverTableRow: 'tblHighlightClass'};
        var tableOptions = {showRowNumber: false, allowHTML: true, 'cssClassNames':cssClasses, 'width': '100%'};  
        var options = {
          title: 'My Daily Activities',
          pieHole: 0.4,
        };

        google.setOnLoadCallback(drawTable1);
        google.setOnLoadCallback(drawTable2);

        google.setOnLoadCallback(drawChart1);
        google.setOnLoadCallback(drawChart2);
        /*
        function drawChart() {

            var data = new google.visualization.DataTable(x);
            var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
            chart.draw(data, options);       
        }*/
        google.setOnLoadCallback(drawChart);

        function drawChart() {
            var data = google.visualization.arrayToDataTable([
              ['Year', 'Sales', 'Expenses'],
              ['2004',  1000,      400],
              ['2005',  1170,      460],
              ['2006',  660,       1120],
              ['2007',  1030,      540]
            ]);

            var options = {
              title: 'Company Performance',
              curveType: 'function',
              legend: { position: 'bottom' }
            };

            var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

            chart.draw(data, options);
        }

         function drawChart1() {
            var x = browserstats
            x.unshift(['browserstats','pageviews'])         
            var data = google.visualization.arrayToDataTable(x);

            var options = {
              pieHole: 0.3,
            };

            var chart = new google.visualization.PieChart(document.getElementById('donutchart-browserstats'));
            chart.draw(data, options);
          }

         function drawChart2() {
            var x = platformstats
            x.unshift(['platformstats','pageviews'])         
            var data = google.visualization.arrayToDataTable(x);

            var options = {
              pieHole: 0.3,
            };

            var chart = new google.visualization.PieChart(document.getElementById('donutchart-platformstats'));
            chart.draw(data, options);
          }

        function drawTable1() {
            var data = new google.visualization.DataTable();
            var rtn = makeTable(data, browserstats)
            var table = new google.visualization.Table(document.getElementById('table-'+rtn[1]));
            table.draw(rtn[0], tableOptions);
        }

        function drawTable2() {
            var data = new google.visualization.DataTable();
            var rtn = makeTable(data, platformstats)
            var table = new google.visualization.Table(document.getElementById('table-'+rtn[1]));
            table.draw(rtn[0], tableOptions);
        }

        function makeTable(data, result){
            console.log(result[0][0])
            console.log()
            for (var i = 0; i < result[0].length; i++) {  
                var typeofresult = typeof result[1][i]
                if (typeofresult == 'object'){
                    var typeofresult = 'string'
                }
                data.addColumn(typeofresult, result[0][i]);
            };
            idname = result[0][0]
            result.shift();
            data.addRows(result);
            return [data,idname];
        }

        var last_width  = window.innerWidth;
        var last_height = window.innerHeight;

        function windowChange(){
            var w = window.innerWidth;
            var h = window.innerHeight;

            if(w != last_width){
                last_width   = w;
                last_height  = h;
                drawRegionsMap();
            }
        }

        var rtime = new Date(1, 1, 2000, 12,00,00);
        var timeout = false;
        var delta = 200;
        $(window).resize(function() {
            rtime = new Date();
            if (timeout === false) {
                timeout = true;
                setTimeout(resizeend, delta);
            }
        });

        function resizeend() {
            if (new Date() - rtime < delta) {
                setTimeout(resizeend, delta);
            } else {
                timeout = false;
                windowChange();
            }               
        }
        //border-color: rgba(0,0,0,.2);      border: 1px solid #ccc;
      
      //box-shadow: 0 2px 10px rgba(0,0,0,.2);
    </script>
    <style type="text/css">
    .tblHeaderClass{ 
        background-color: #5cb85c;

    }
    .google-visualization-table-th, .google-visualization-table-td{
        border: 0px;
    }
    #table_div { 
        min-width: 300px;
    }
    .floatleft{
        float: left;
        width: 100%;
    }
    .donutchart{
        float: left;
        width: 100%;
        min-height: 200px;
    }
    .curve_chart{
        width: 100%;
        min-height: 250px;
    }

    </style>


<div class="container">
    <div class="row">
        <?php include 'sidebar.php'; ?> 
        <div class="col-sm-9 col-md-9">

        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-stats">
                    </span> Browserstats</a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in" >
                <div class="panel-body">
                    <div class="row">
                        <div class="col-sm-12 col-md-12">
                            <div id="curve_chart" class="curve_chart"></div>
                           
                        </div>
                    </div>
                    
                    
                </div>
            </div>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-map-marker">
                    </span> Platformstats</a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in">
                <div class="panel-body">
                    <div class="row">
                        <div class="col-sm-6 col-md-6">
                            <div id="donutchart-platformstats" class="donutchart"></div>
                        </div>
                        <div class="col-sm-6 col-md-6">
                            <div id="table-platformstats" class="floatleft"></div> 
                        </div>
                    </div>
                    
                    

                </div>
            </div>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-stats">
                    </span> Browserstats</a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in" >
                <div class="panel-body">
                    <div class="row">
                        <div class="col-sm-6 col-md-6">
                            <div id="donutchart-browserstats" class="donutchart"></div>
                        </div>
                        <div class="col-sm-6 col-md-6">
                           <div id="table-browserstats" class="floatleft"></div> 
                        </div>
                    </div>
                    
                    
                </div>
            </div>
        </div>
            
        </div>
    </div>
</div>