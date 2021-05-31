<?php
$args = $_POST["args"];
echo $args;

try {
    $com = 'python ../PythonBackend/runner_script.py ' . $args;
    $command = escapeshellcmd($com);
    $output = shell_exec($command);

    echo json_encode($output);
} catch (Exception $e) {
    echo $e;
}
