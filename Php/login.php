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
    mkdir($path,0777);
    chmod($path,0777);
    
    echo '<script type="text/javascript">';
    echo "sessionStorage.setItem('name','".$str_exploded[0] ."');";
    echo "sessionStorage.setItem('email','".$email."');";
    echo "window.location.href = '../Pages/Index.html';";
    
    
    echo "</script>";

    //header("Location: ../Pages/Index.html");
} else {
    echo "THIS SHOULD BE TECHINCALLY INACCESSIBLE";
    echo "User not found";
}
?>
