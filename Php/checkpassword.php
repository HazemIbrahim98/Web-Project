<?php
require_once "connect.php";

$email = $_POST["email"];
$password = sha1($_POST["password"]);

$sql = "SELECT * FROM `users` WHERE email = '" . $email . "' AND password = '" . $password . "'";

$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);

if ($row)
    echo "Ok";
else
    echo "Password Mismatch";
?>