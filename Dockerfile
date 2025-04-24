FROM rust:1.70 as builder
WORKDIR /app
COPY . .
RUN cargo build --release

FROM debian:bullseye-slim
COPY --from=builder /app/target/release/bsc-auto-trader .
COPY config/ ./config/
CMD ["./institutional-bsc-pro", "--config", "config/main.yaml"]
