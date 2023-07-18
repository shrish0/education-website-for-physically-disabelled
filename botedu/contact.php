<?php
      $login=false;
      $server="localhost";
      $username="root";
      $password="";

      $con=mysqli_connect($server,$username,$password);
      if(!$con)
      {
        die("connection to this database failed due to " .mysqli_connect_error());
      }
      
      $name=$_POST['name'] ;
      $email=$_POST['email'];
      $subject=$_POST['subject'];
      $message=$_POST['message'];
      $sql="INSERT INTO `shri`.`contact` (`name`, `subject`, `email`,`message`) VALUES ('$name', '$subject', '$email','$message');
      ";
    //   echo $sql;
      if($con->query($sql)==true)
      {
        echo "success";
        $login=true;
        header("location:contact.html");
      }
      $con->close();

?>
</body>
</html>