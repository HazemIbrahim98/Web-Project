<?php
//echo "Working";

$args = $_POST["args"];
echo $args;

try{
    $command = escapeshellcmd('python3 /opt/lampp/htdocs/Web-Project/PythonBackend/runner_script.py 0 3 [[12,relu],[8,relu],[4,sigmoid]] 10');
    $output = shell_exec($command);
    //echo json_encode($output);
    
    
}
catch (Exception $e)
{
    echo $e;
}
