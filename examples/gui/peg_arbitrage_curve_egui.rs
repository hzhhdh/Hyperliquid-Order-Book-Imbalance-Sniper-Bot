use eframe::{egui, epi};
struct App;
impl epi::App for App {
    fn update(&mut self, ctx: &egui::CtxRef, _: &epi::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            if ui.button("Start Curve Arbitrage").clicked() { /* trigger */ }
            if ui.button("Stop Curve Arbitrage").clicked()  { /* stop */ }
        });
    }
    fn name(&self) -> &str { "Curve Arbitrage" }
}
