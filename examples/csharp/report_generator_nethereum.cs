using System.IO;
var csv = new StringBuilder();
csv.AppendLine("Wallet,PnL");
foreach(var w in wallets){ csv.AppendLine($"{w.Address},{w.PnL}"); }
File.WriteAllText("report.csv", csv.ToString());
