use tauri::Builder;
fn main() {
    Builder::default()
        .invoke_handler(tauri::generate_handler![set_deposit, set_leverage])
        .run(tauri::generate_context!())
        .expect("error while running Tauri app");
}
// Commands exposed to frontend:
#[tauri::command]
fn set_deposit(amount: f64) { /* store in config */ }
#[tauri::command]
fn set_leverage(ratio: u8) { /* store in config */ }
