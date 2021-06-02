<?php
$args = $_POST["args"];

try {
    $com = 'python ../PythonBackend/runner_script.py ' . $args;
    $command = escapeshellcmd($com);
    $output = shell_exec($command);

    session_start();

    $_SESSION["modelOutput"] = $output;
    $str_explode = explode("\n", $output);

    echo $str_explode[0];
} catch (Exception $e) {
    echo $e;
}
