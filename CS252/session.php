<?php
session_start();
include('connection.php');
$username=$_POST['username'];
$password=$_POST['password'];
$query = "SELECT *
        FROM member
        WHERE username = '$username';";
$result = mysql_query($query);

$userData = mysql_fetch_array($result, MYSQL_ASSOC);

if(mysql_num_rows($result) == 0) // User not found. So, redirect to login_form again.
{
    header('Location: login.php');
}
else
{
    $_SESSION['loggedin'] = true;
    $_SESSION['username'] = $userData['username'];
    $_SESSION['id'] = $userData['mem_id'];
    
    header('Location: index.php');
}
?>
