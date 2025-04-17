<?php
require 'vendor/autoload.php';
$web3 = new Web3\Web3('http://localhost:8545');
$web3->txpool->contentious(function($err,$txs){ var_dump($txs); });
