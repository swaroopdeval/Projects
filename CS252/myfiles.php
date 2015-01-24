<!DOCTYPE html>
<html>
<body>
<?php
//Start session
session_start();
include('connection.php');
$name= $_SESSION['username'];
$id= $_SESSION['id'];
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == true)
{
    $result=mysql_query("SELECT * FROM files");
    //echo $result;
    if (!$result) { // add this check.
    die('Invalid query: ' . mysql_error());
    }
    while($row = mysql_fetch_array($result)) 
    {
    echo $row['mem_id'] . " " . $row['fname'];
    echo "<br>";
    }

}
 else
{
    header("location: login.php");
}
?>
<a href="index.php">Home</a><br>
<a href="signout.php">Sign Out</a>
</body>
</html>
