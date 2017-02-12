<?php

# takes in csv
#symbol, #current price, current owned (from fidelity)
#on file for main account, one file for all retirement acounts(created manually probably)
# config file with % of each
$ini_file = "percentages.ini";
$percents = parse_ini_file($ini_file);
var_dump($percents);
$portfolio_file = "joint.tsv";
$lines = file($portfolio_file);
$portfolio_array = array();
$totalWorth = 0;
foreach ($lines as $line){
  list ($symbol,$amount_owned,$current_price) = explode("\t",$line);
  if($symbol == "Symbol"){
    continue;
  }
  $current_price =substr(trim($current_price),1);
  $worth = $amount_owned * $current_price;
  $totalWorth += $worth;
  $details = array();
  $details['owned'] = $amount_owned;
  $details['price'] = $current_price;
  $details['owned_worth'] = $worth;

  if(isset($percents[$symbol])){
    $details['standard_percent'] = $percents[$symbol] / 100;
  }else{
    $details['standard_percent'] = 0;
  }
#$details['amount_to_sell'] = "";
#$details['a,

  $portfolio_array[$symbol] = $details;

}

foreach($percents as $symbol =>$percent){
  if(!isset($portfolio_array[$symbol])){
    die ("error $symbol not found in $portfolio_file but is in $ini_file, it must be in both if in $ini_file");
  }
}
$filename = "output.csv";
$handle = fopen($filename, "w");
$top_line = "symbol,buy/sell amount,price,current owned,current worth,current percent,standard percent,difference percent,difference worth,buy/sell amount\n";
fwrite($handle,$top_line);
foreach($portfolio_array as $symbol => $details){
  $owned_percent = $details['owned_worth'] / $totalWorth;
  $details['owned_percent'] = $owned_percent;
  $difference_percent = $details['standard_percent'] - $owned_percent ;
  $difference_worth = $difference_percent * $totalWorth;
  $difference_amount = $difference_worth / $details['price'];
  $details['difference_percent'] = $difference_percent;
  $details['difference_worth'] = $difference_worth;
  $details['difference_amount'] = $difference_amount;
  $portfolio_array[$symbol] = $details;
  $difference_amount_rounded = round($difference_amount);
  $outputString = "$symbol,$difference_amount_rounded,{$details['price']},{$details['owned']},{$details['owned_worth']},$owned_percent,{$details['standard_percent']},$difference_percent,$difference_worth,$difference_amount_rounded\n";
  fwrite($handle, $outputString);
}
fclose($handle);
var_dump($portfolio_array);
