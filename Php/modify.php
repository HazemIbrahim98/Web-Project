<?php
require_once "connect.php";

$email = $_POST["email"];
$password = sha1($_POST["password"]);

$sql = "UPDATE `users` SET password = '" . $password . "' WHERE email = '" . $email . "'";

$result = mysqli_query($conn, $sql);
echo "THIS IS FORM PHP";

mysqli_close($conn);
