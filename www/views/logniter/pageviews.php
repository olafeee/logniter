
 <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
        var json_data = <?php echo $this->register->result; ?>

        var period = <?php echo $this->register->period; ?>
    
        

        switch(period) {
            case "pageviewspermonth":
                period = 'montname'
                break;
            case "pageviewsperweek":
                period = 'weekname'
                break;
            default:
                console.log('no things where found')
        }
        var pageviews = [[period,'pageviews'],];

        if(json_data['returndata']){
            json_data = json_data['returndata'];
            //var obj = JSON.parse(json);

            for(var i in json_data)
                pageviews.push([json_data[i][period],json_data[i]['pageviews']]);
        }
        console.log(pageviews)

        google.load("visualization", "1", {packages:["geochart","table","corechart",,"bar"]});


        google.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable(pageviews);

        var options = {
          chart: {
            title: 'Company Performance',
            subtitle: 'Sales, Expenses, and Profit: 2014-2017',
          }
        };

        var chart = new google.charts.Bar(document.getElementById('columnchart_material'));

        chart.draw(data, options);
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
<div class="alert alert-danger" role="alert"></div>

  <div class="input-group">
      <div class="input-group-btn">
        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Action <span class="caret"></span></button>
        <ul class="dropdown-menu">
          <li><a href="#">year</a></li>
          <li><a href="#">Another action</a></li>
          <li><a href="#">Something else here</a></li>
          <li role="separator" class="divider"></li>
          <li><a href="#">Separated link</a></li>
        </ul>
      </div><!-- /btn-group -->
      <input type="year" class="form-control" aria-label="..." >
    </div><!-- /input-group -->

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
                            <div id="columnchart_material" class="curve_chart"></div>
                           
                        </div>
                    </div>
                    
                    
                </div>
            </div>
        </div>

            
        </div>
    </div>
</div>