<?php
require_once "connect.php";

$emaill = $_POST["email"];

$sql = "SELECT * FROM `users` WHERE email = '" . $emaill . "'";
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);


if ($row) {
    echo "Email Exists";
} else
    echo "Ok";
