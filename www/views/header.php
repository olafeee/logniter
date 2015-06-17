<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Olaf Elzinga</title>

    <!-- Bootstrap -->
    <link href="/css/sb-admin.css" rel="stylesheet">
    <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="/css/style.css" rel="stylesheet">


<script src="//code.jquery.com/jquery-1.10.2.js"></script>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>

<script src="/js/jquery.mobile.custom.min.js"></script>

<script src="http://code.highcharts.com/highcharts.js"></script>
<script src="http://code.highcharts.com/maps/modules/map.js"></script>
<script src="http://code.highcharts.com/maps/modules/data.js"></script>
<script src="http://code.highcharts.com/mapdata/custom/world.js"></script>


    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
  
  <body>
    <!-- opacity div for the SLA info menu-->
  <div id="wrap">

      <!-- Fixed navbar -->
<nav class="navbar nav-div navbar-default" role="navigation">
  <!-- Brand and toggle get grouped for better mobile display -->
  <div class="navbar-header">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>
    
  </div>

  <!-- Collect the nav links, forms, and other content for toggling -->
  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
   <div class="container">
    <ul class="nav navbar-nav">
      <li><a href="/">Home</a></li>
      <li><a href="/order">Order</a></li>
      <li><a href="/projects">Projects</a></li>

    </ul>
    <ul class="nav navbar-nav nav-right">
      <?php
      if(Session::get('loggedIn') == true){
        echo'<li><a href="/account/account">Account</a></li>';
      }
      if(Session::get('loggedIn') == true){
        echo'<li><a href="/account/logout">Logout</a></li>';
      }else{
        echo'<li><a href="/account/">Login</a></li>';
      }?>  
    </ul>
    </div>
  </div><!-- /.navbar-collapse -->
</nav>

      <!-- Begin page content -->
        