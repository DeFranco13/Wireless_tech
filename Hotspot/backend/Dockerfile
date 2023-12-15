FROM rust:1.74.1-slim-bookworm as build

COPY ./Cargo.* ./

COPY ./src ./src
RUN cargo build --release


FROM debian:bookworm-slim
COPY --from=build ./target/release/backend ./api

CMD ["./api"]
EXPOSE 8080
