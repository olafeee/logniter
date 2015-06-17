<script type="text/javascript">
    function myFunction() {
        var begindate = document.getElementById("begindate").value
        var enddate = document.getElementById("enddate").value

        if (begindate && enddate){
            window.location.assign("http://www.olafelzinga.com/pageviews/"+begindate+'/'+enddate);
        }  
    } 

    function dateChecker(){
        var begindate = new Date(document.getElementById("begindate").value);
        var enddate = new Date(document.getElementById("enddate").value);

        if(begindate.getFullYear() > enddate.getFullYear()){
            change()
        }else if (begindate.getMonth() > enddate.getMonth() && begindate.getFullYear() == enddate.getFullYear()) {
            change()
        }else if (begindate.getDate() > enddate.getDate() && begindate.getMonth() == enddate.getMonth() && begindate.getFullYear() == enddate.getFullYear()) {
            change()
        }

        function change(){
            var currentMonth = enddate.getMonth()
            if (currentMonth < 10) { currentMonth = '0' + currentMonth; }
            var day = enddate.getDate()
            enddate = enddate.getFullYear()+'-'+currentMonth+'-'+day
            document.getElementById("begindate").value  = document.getElementById("enddate").value
        }

    }

</script>

<div class="col-sm-3 col-md-3">
    <div class="panel-group" id="accordion">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-folder-close">
                    </span> Content</a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in">
                <div class="panel-body">
                    <table class="table">
                        <tr>
                            <td>
                                <span class="glyphicon glyphicon-th-large"></span><a href="/logniter"> Home</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <span class="glyphicon glyphicon-th-large"></span><a href="/logniter/pageviews/"> Page views</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <span class="glyphicon glyphicon-th-large"></span><a href="/logniter/clientstats/"> Platform stats</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <span class="glyphicon glyphicon-map-marker"></span><a href="/logniter/pageviewspercountry/"> World map</a>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo"><span class="glyphicon glyphicon-th">
                    </span> Options</a>
                </h4>
            </div>
            <div id="collapseTwo" class="panel-collapse collapse">
                <div class="panel-body">
                    <table class="table">
                        <tr>
                            <td>
                                <a href="http://www.jquery2dotnet.com">Orders</a> <span class="label label-success">$ 320</span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <form>
                                    <div class="input-group">
                                      <span class="input-group-addon" id="basic-addon1"><span class="glyphicon glyphicon-calendar"></span></span>
                                      <input type="date" id="begindate" name="begindate" onchange="dateChecker()" />
                                    </div>

                                    <div class="input-group">
                                      <span class="input-group-addon" id="basic-addon1"><span class="glyphicon glyphicon-calendar"></span></span>
                                      <input type="date" id="enddate" name="enddate" onchange="dateChecker()" />
                                    </div>
                                    <input type="button" onclick="myFunction()" value="Submit form">
                                </form>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>


    </div>
</div>