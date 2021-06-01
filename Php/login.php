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
    $str_exploded = explode("@",$_SESSION["email"]);
    $_SESSION["name"] = $str_exploded[0];
    $path = "../Dataset/".$_SESSION["name"];
    mkdir($path,777);
    header("Location: ../Pages/Index.html");
} else {
    echo "THIS SHOULD BE TECHINCALLY INACCESSIBLE";
    echo "User not found";
}
