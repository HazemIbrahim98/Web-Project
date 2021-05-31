<?php
echo "Working";

$args = $_POST["args"];
echo $args;

$command = escapeshellcmd('python C:/xampp/htdocs/Web-Project/PythonBackend/runner_script.py 0 3 [[12,4,relu],[8,4,relu],[4,2,sigmoid]] 1');
$output = shell_exec($command);
echo $output;
