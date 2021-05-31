<?php
require_once "connect.php";

$email = $_POST["email"];
$password = sha1($_POST["password"]);


//Make sure user doesn't exist
$sql = "SELECT * FROM `users` WHERE email = '" . $email . "'";

$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);
if ($row) {
    echo "Email already Exists!";
} else {
    $sql = "INSERT INTO `users`(`email`, `password`) VALUES ('" . $email . "','" . $password . "')";
    mysqli_query($conn, $sql);
    header("Location: ../Pages/Index.html");
}
