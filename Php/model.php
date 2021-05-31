<?php
$args = $_POST["args"];
echo $args;

$com = 'python C:/xampp/htdocs/Web-Project/PythonBackend/runner_script.py ' . $args;
$command = escapeshellcmd($com);
$output = shell_exec($command);

echo json_encode($output);
