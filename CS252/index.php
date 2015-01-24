<!DOCTYPE html>
<html>
<body>
<?php
//Start session
session_start();
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == true) 
{
    echo "Welcome, " . $_SESSION['username'] . "!<br>";
    echo "Your id is: ". $_SESSION['id'];
}
 else 
{
    header("location: login.php");
}
?>
<form action="upload_file.php" method="post"
enctype="multipart/form-data">
<label for="file">Filename:</label>
<input type="file" name="file" id="file"><br>
<input type="submit" name="submit" value="Submit">
</form>
<a href="myfiles.php">My Files</a><br>
<a href="signout.php">Sign Out</a>
</body>
</html>
