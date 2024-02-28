<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "sentiment";

$con = mysqli_connect("localhost","username","password","dbname","txtPhone");

$user_username = $_POST['username'];
$user_password = $_POST['password'];
$txtPhone = $_POST['txtPhone'];
$user_email = $_POST['email'];
$sql = "INSERT INTO 'login' ('username','password','email') VALUES ('$user_username', '$user_password', '$user_email');"
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Contact Records Inserted";
}
else
{
    echo "error";
}
$conn->close();