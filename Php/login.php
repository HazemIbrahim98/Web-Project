<?php
session_start();
require_once "connect.php";

$email = $_POST["email"];
$password = $_POST["password"];

$sql = "SELECT * FROM `users` WHERE email = '" . $email . "' AND password = '" . $password . "'";

$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);
$_SESSION["UserID"] = $row[0];

$url = 'http://localhost:85/WebProject/Pages/Index.html';
