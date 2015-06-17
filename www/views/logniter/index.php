 <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
        json_country <?php //$pageviewspercountry ?>
        google.load("visualization", "1", {packages:["geochart"]});
        google.setOnLoadCallback(drawRegionsMap);

        function drawRegionsMap() {

        var data = google.visualization.arrayToDataTable([
          ['Country', 'Popularity'],
          ['Germany', 200],
          ['United States', 300],
          ['Brazil', 400],
          ['Canada', 500],
          ['France', 600],
          ['RU', 700],
          ['NL', 900],
          ['Austria',200]
        ]);

        var options = {};

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

/*
$(function() {
  // Bind an event handler to window throttledresize event that, when triggered,
  // passes a reference of itself that is accessible by the callback function.
  $( window ).on( "throttledresize", throttledresizeHandler );
 
  function throttledresizeHandler( event ) {
    windowChange();
  }
});*/
    </script>

    


<!--

<style type="text/css">
${demo.css}
    </style>
<script type="text/javascript">

json_data = <?php //echo $json_data; ?>

$(function () {
    $('#container').highcharts({
        chart: {
            type: 'bar',
            backgroundColor: '#f5f5f5'
        },
        title: {
            text: 'Daily page'
        },
        subtitle: {
            text: 'olafelzinga.com'
        },
        xAxis: {
            categories: json_data["datetime"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'views',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' millions'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: false
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#f5f5f5'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'page',
            data: json_data["page"]
        }, {
            name: 'hit',
            data: json_data["hit"]
        }]
    });
});
    </script>
-->
<div class="container">
    <div class="row">
        <?php include 'sidebar.php'; ?> 
        <div class="col-sm-9 col-md-9">
            <div id="regions_div" style="height: 100%;width: 100%;margin:auto;background:#fff;text-align:center"></div>
            <!--
            <div class="info_box">
                

                <h1>

                    Accordion Menu With Icon</h1>
                Balphenaar Dashboard Afffccordion Menu
                <div id="container" style="min-width: 260px; height: 400px; margin: 0 auto"></div>
                <div class="table-accesslog">
                    <table class="table table-striped">
                        <tr class="table-accesslog-tr">
                            <td class="table-accesslog-td">Hour</td><td class="table-accesslog-td">Page</td><td class="table-accesslog-td">Hit</td>
                        </tr>
                        <?php
                        //echo "<pre>"; print_r($json_dict); echo "</pre>";
                        //foreach ($json_dict as $key => $value) {
                        //    echo '<tr><td class="table-accesslog-td">'.$value["datetime"].'</td>';
                        //    echo '<td class="table-accesslog-td">'.$value["page"].'</td>';
                        //   echo '<td class="table-accesslog-td">'.$value["hit"].'</td></tr>';
                        //}

                         ?>
                    </table>
                </div>

            </div> -->
        </div>
    </div>
</div>

<!--
<script src="/js/highchart/highcharts.js"></script>

<script src="http://code.highcharts.com/modules/map.js"></script>
<script src="/js/modules/data.js"></script>
<script src="/js/modules/exporting.js"></script>
<script src="http://code.highcharts.com/mapdata/custom/world.js"></script>



<?php //echo $this->register->test; ?>

<style type="text/css">
#container {
    height: 500px; 
    min-width: 310px; 
    max-width: 800px; 
    margin: 0 auto; 
}
.loading {
    margin-top: 10em;
    text-align: center;
    color: gray;
}
</style>

<script type="text/javascript">
json_country = <?php echo $json_country; ?>   

$(function () {


        // Initiate the chart
        $('#container').highcharts('Map', {

            title : {
                text : 'Zoom in on country by double click'
            },

            mapNavigation: {
                enabled: true,
                enableDoubleClickZoomTo: true
            },

            colorAxis: {
                min: 1,
                max: 1000,
                type: 'logarithmic'
            },

            series : [{
                data : json_country,
                mapData: Highcharts.maps['custom/world'],
                joinBy: ['iso-a2', 'code'],
                name: 'Population density',
                states: {
                    hover: {
                        color: '#BADA55'
                    }
                },
                tooltip: {
                    valueSuffix: '/km²'
                }
            }]
        });
});
        </script>




       



<div class="container">
<div class="row">
      
        <?php include 'sidebar.php'; ?> 
        <div class="col-sm-9 col-md-9">
            <div class="info_box">

<div id="container" style="max-width: 1000px"></div>


            </div>
        </div>
    </div>
</div>-->