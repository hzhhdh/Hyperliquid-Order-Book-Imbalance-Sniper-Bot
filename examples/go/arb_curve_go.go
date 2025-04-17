package main
func main(){
  price := getCurvePrice()
  if math.Abs(price-1) > 0.005 { executeArb() }
}
