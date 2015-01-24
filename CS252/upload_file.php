<?php
session_start();
include('connection.php');

$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["file"]["name"]);
$extension = end($temp);
$id=$_SESSION['id'];
$fname=$_FILES["file"]["name"];

if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 20000)
&& in_array($extension, $allowedExts)) {
  if ($_FILES["file"]["error"] > 0) {
    echo "Return Code: " . $_FILES["file"]["error"] . "<br>";
  } else {
    echo "Upload: " . $_FILES["file"]["name"] . "<br>";
    echo "Type: " . $_FILES["file"]["type"] . "<br>";
    echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
    echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br>";
    if (file_exists("/home/jeet/Pictures/" .$_SESSION['username']."_".$_FILES["file"]["name"])) {
      echo $_FILES["file"]["name"] . " already exists. ";
    } else {
       mysql_query("INSERT INTO files(mem_id, fname)VALUES('$id','$fname')");
      move_uploaded_file($_FILES["file"]["tmp_name"],
      "/home/jeet/Pictures/" .$_SESSION['username']. "_".$_FILES["file"]["name"]);
      echo "Stored in: " . "/home/jeet/Pictures/" . $_FILES["file"]["name"];
    }
  }
} else {
  echo "Invalid file";
}
?>
