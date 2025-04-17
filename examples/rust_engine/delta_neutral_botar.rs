use botvana::Strategy;
fn main() {
    let mut strat = Strategy::new("delta_neutral", config);
    strat.on_event(|e| strat.process(e));
    strat.run().unwrap();
}
