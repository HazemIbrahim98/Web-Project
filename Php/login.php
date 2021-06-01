<?php
session_start();
require_once "connect.php";

$email = $_POST["email"];
$password = sha1($_POST["password"]);

$sql = "SELECT * FROM `users` WHERE email = '" . $email . "' AND password = '" . $password . "'";

$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);

if ($row) {
    session_start();
    $_SESSION["email"] = $row["email"];
    header("Location: ../Pages/Index.html");
} else {
    echo "THIS SHOULD BE TECHINCALLY INACCESSIBLE";
    echo "User not found";
}
