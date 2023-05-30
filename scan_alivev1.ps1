$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Tu gateway: $subred"

$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3 )
echo $rango

$punto = $rango.EndWith('.')
if ( $punto -like "False" )
{
    $rango = $rango + '.'
}

$rango_ip = @(1..254)

foreach ( $r in $rango_ip)
{
    $actual = $rango + $r
    $response = Test-Connection $actual -Quiet -Count 1
    if ($response -eq "True" )
    {
        Write-Output ""
        Write-Host " Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}