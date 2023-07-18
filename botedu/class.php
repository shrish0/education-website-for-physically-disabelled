<?php
$class=$_GET['class'];
$subject=$_GET['subject'];

?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Courses</title>
  <meta content="" name="description">
  <meta content="" name="keywords">
  <link href="assets/vendor/animate.css/animate.min.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="assets/vendor/remixicon/remixicon.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="allclass.css" rel="stylesheet">

  <link href="assets/css/style.css" rel="stylesheet">

</head>

<body>

  <header id="header" class="fixed-top">
    <div class="container d-flex align-items-center">

      <h1 class="logo me-auto"><a href="index.html"><b>EDUFREE</b></a></h1>

      <nav id="navbar" class="navbar order-last order-lg-0">
      <ul>
          <li><a class="active" href="index.html" id="home">Home</a></li>
          <li><a href="about.html" id="about">About</a></li>
          <li><a href="courses.php" id="courses">Courses</a></li>
          <li><a href="contact.html" id="contact">Contact</a></li>
        </ul>
        <i class="bi bi-list mobile-nav-toggle"></i>
      </nav>

      <a href="courses.html" class="get-started-btn">Get Started</a>

    </div>
  </header>

  <main id="main" data-aos="fade-in">

    <div class="breadcrumbs">
      <div class="container">
      <h2>
  <?php echo $class;?><br>
  
      </div>
    </div>
    <section>
      <section>

<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'class10')" id="defaultOpen">Chapter 1</button>
  <button class="tablinks" onclick="openCity(event, 'Class 9')">Chapter 2</button>
  <button class="tablinks" onclick="openCity(event, 'Class 8')">Chapter 3</button>
  <button class="tablinks" onclick="openCity(event, 'Class 7')">Chapter 4</button>
  <button class="tablinks" onclick="openCity(event, 'Class 6')">Chapter 5</button>
  <button class="tablinks" onclick="openCity(event, 'Class 5')">Chapter 6</button>
</div>

<div id="class10" class="tabcontent">
  <h3 class="class_1" ><u><?php echo $subject;?></h2></u></h3>
  <div class="Math">
    
 <div class="chapter_1" id="c1">
 <iframe width="900" height="550" src="https://www.youtube.com/embed/-tb6KrlXEJ0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen id="if1
  "></iframe>
 </div> 
 Pdf Download
    </div>
    </div>

</div>

<div id="Class 9" class="tabcontent" >
<h3 class="class_1" ><u><?php echo $subject;?></h2></u></h3>
  <div class="chapter_1" id="c2">
  <iframe width="900" height="550" src="https://www.youtube.com/embed/ui1y_ZioSgA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  Pdf download
</div>
    </div>
</div>

<div id="Class 8" class="tabcontent">
<h3 class="class_1" ><u><?php echo $subject;?></h2></u></h3>
  <div class="chapter_1" id="c3">
  <iframe width="900" height="550" src="https://www.youtube.com/embed/nzQ8OGu2N5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  Pdf download
</div>
</div>

<div id="Class 7" class="tabcontent">
<h3 class="class_1" ><u><?php echo $subject;?></h2></u></h3>
  <div class="chapter_1" id="c4">
  <iframe width="900" height="550" src="https://www.youtube.com/embed/cM0StvAxa3g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  Pdf download
</div>
</div>
<div id="Class 6" class="tabcontent">
<h3 class="class_1" ><u><?php echo $subject;?></h2></u></h3>
  <div class="chapter_1" id="c5">
  <iframe width="900" height="550" src="https://www.youtube.com/embed/TgoWFEIm01g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  Pdf download
</div>
</div>
<div id="Class 5" class="tabcontent">
<h3 class="class_1" ><u><?php echo $subject;?></h2></u></h3>
  <div class="chapter_1" id="c6">
  <iframe width="900" height="550" src="https://www.youtube.com/embed/ieJCOO2Vew4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  Pdf download
</div>
</div>
       </section>
    </section>
    </div>
    </div>
    </div>
    </div>

    </div>

    </div>
    </section>

  </main>
  <footer id="footer">

    <div class="footer-top">
      <div class="container">
        <div class="row">

          <div class="col-lg-3 col-md-6 footer-contact">
            <h3>Mentor</h3>
            <p>
             Street <br>
              New delhi, NY 535022<br>
              India<br><br>
              <strong>Phone:</strong> +910000000000<br>
              <strong>Email:</strong> info@example.com<br>
            </p>
          </div>

        </div>
      </div>
    </div>

    <div class="container d-md-flex py-4">

      <div class="me-md-auto text-center text-md-start">
        <div class="copyright">
          &copy; Copyright <strong><span>Edufreee</span></strong>. All Rights Reserved
        </div>
      </div>
    </div>
  </footer>

  <div id="preloader"></div>
  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i
      class="bi bi-arrow-up-short"></i></a>

  <script src="assets/vendor/purecounter/purecounter_vanilla.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/js/main.js"></script>
  <script src="class.js"></script>

</body>

</html>