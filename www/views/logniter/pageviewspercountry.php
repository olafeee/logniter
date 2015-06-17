
 <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
        var json_data = <?php echo $this->register->pageviewspercountry; ?>

        
        var result = [['Country', 'Pageviews'],];

        if(json_data['returndata']){
            json_data = json_data['returndata'];
            //var obj = JSON.parse(json);

            for(var i in json_data)
                result.push([json_data[i]['countrycode'],json_data[i]['pageviews']]);


        }else{
            result.push(['Congo', 400],['China', 100],['Chile', 200])          
        }
        google.load("visualization", "1", {packages:["geochart","table"]});
        google.setOnLoadCallback(drawRegionsMap);

        //googletable.load("visualization", "1", {packages:["table"]});
        google.setOnLoadCallback(drawTable);

        function drawTable() {
            var data = new google.visualization.DataTable();
            var data = new google.visualization.DataTable();
            for (var i = 0; i < result[0].length; i++) {
                data.addColumn(typeof result[1][i], result[0][i]);
            };
            result.shift();
            data.addRows(result);

            var table = new google.visualization.Table(document.getElementById('table_div'));
            var cssClasses = {headerRow: 'tblHeaderClass',hoverTableRow: 'tblHighlightClass'};
            var options = {showRowNumber: false, allowHTML: true, 'cssClassNames':cssClasses, 'width': '100%'};

            table.draw(data, options);
        }

        function drawRegionsMap() {

        var data = google.visualization.arrayToDataTable(result)
        
        var options = {};
        options['colorAxis'] = { minValue : 1, colors : ['#EBFFFC','#05FFD5']};
        options['backgroundColor'] = '#FFF';

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
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

    </style>


<div class="container">
    <div class="row">
        <?php include 'sidebar.php'; ?> 
        <div class="col-sm-9 col-md-9">

        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-map-marker">
                    </span>World map</a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in">
                <div class="panel-body">
                    <div id="regions_div" style="height: 100%;width: 100%;margin:auto;background:#fff;text-align:center"></div>
                </div>
            </div>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-stats">
                    </span>Stats</a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in" >
                <div class="panel-body" style="padding: 0px;">
                    <div id="table_div"></div> 
                </div>
            </div>
        </div>
            
        </div>
    </div>
</div>