<div align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,45:0e7490,100:14b8a6&height=215&section=header&text=Kunal&fontSize=56&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Rust%20Backend%20Engineer%20%7C%20Distributed%20Systems%20%7C%20Blockchain%20Infrastructure&descAlignY=58&descSize=16"
    width="100%"
    alt="Kunal — Rust backend engineer"
  />

  <a href="https://git.io/typing-svg">
    <img
      src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1400&color=22D3EE&center=true&vCenter=true&width=900&lines=Matching+engines+with+deterministic+state;Authenticated+networking+on+Linux;Solana+programs%2C+indexers%2C+and+event+pipelines"
      alt="Matching engines, authenticated networking, and blockchain infrastructure"
    />
  </a>
</div>

<p align="center">
  <a href="https://kunalagarawal.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-0F766E?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" />
  </a>
  <a href="https://www.linkedin.com/in/kunal-r6/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:kunalkunal63@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://drive.google.com/file/d/1Aw6KtOZdKzJP9aORcOHwPvyKZkWzcfZx/view?usp=drive_link">
    <img src="https://img.shields.io/badge/Resume-334155?style=for-the-badge&logo=googledrive&logoColor=white" alt="Resume" />
  </a>
  <a href="https://drive.google.com/file/d/1u2NoEQygw5iVl_k_af0xoAMGgW5CaJ7y/view?usp=sharing">
    <img src="https://img.shields.io/badge/Blockchain_resume-7C3AED?style=for-the-badge&logo=googledrive&logoColor=white" alt="Blockchain resume" />
  </a>
</p>

## Hello, I am Kunal

I build trading, networking, and blockchain systems in Rust. My projects range from an authenticated Linux VPN to matching engines and a Solana central limit order book.

I am most interested in the parts that are easy to hide in a demo but difficult to get right: deterministic state transitions, replay, failure recovery, bounded on-chain execution, ownership, and safe resource cleanup. I document unfinished pieces and design tradeoffs alongside the code.

## Selected systems

| Project | Engineering focus | Status |
|---|---|---|
| **[Tidebook](https://github.com/kunal171/tidebook)** | Solana CLOB with collateralized orders, price-level FIFO queues, bounded atomic matching, fee accounting, a Next.js client, and a Rust indexer | Active research build |
| **[HFT Limit Order Book](https://github.com/kunal171/hft-limit-order-book)** | Deterministic price-time matching, O(1) cancellation, replayable events, simulation, benchmarks, and a PostgreSQL control plane | Engine and API built; integration next |
| **[Rust VPN](https://github.com/kunal171/rust_vpn)** | Linux TUN over UDP with X25519, Ed25519, ChaCha20-Poly1305, replay protection, routing, DNS handling, and cleanup | Personal beta; not security-audited |
| **[Subdex](https://github.com/kunal171/subdex)** | Code-first Substrate indexer for chain ingestion and backend data pipelines | In development |
| **[Distributed Queue](https://github.com/kunal171/distributed_queue)** | TCP message broker with multiple producers and consumers and at-least-once delivery | Learning implementation |
| **[Raft Consensus](https://github.com/kunal171/raft_consensus)** | Leader election, replication, and consensus experiments in Rust | Learning implementation |

<details>
<summary><strong>Earlier backend projects</strong></summary>

- [gRPC task service](https://github.com/kunal171/grpc_service) — unary, server-streaming, and bidirectional Tonic RPCs.
- [URL shortener](https://github.com/kunal171/url_shortner) — Axum, Tokio, MongoDB, validation, redirects, and visit statistics.
- [Redis clone](https://github.com/kunal171/redis_clone) — RESP parsing and an asynchronous in-memory store.
- [Mini blockchain](https://github.com/kunal171/blockchain) — blockchain fundamentals over a peer-to-peer gossip network.

</details>

## Systems toolbox

| Area | Tools and concepts |
|---|---|
| Rust backend | Rust, Tokio, Axum, Actix Web, Tonic/gRPC, channels, structured errors |
| Trading systems | Price-time priority, order books, integer arithmetic, event replay, simulation, latency measurement |
| Networking | TCP/UDP, Linux TUN, routing, network namespaces, DNS, packet validation |
| Cryptography | X25519, Ed25519, ChaCha20-Poly1305, authenticated encryption, replay protection |
| Blockchain | Solana, Anchor, Substrate, Polkadot, smart contracts, event indexers |
| Data and operations | PostgreSQL, MongoDB, Redis, Docker, GitHub Actions, metrics and tracing |

<p align="center">
  <img src="https://skillicons.dev/icons?i=rust,ts,solidity,postgres,redis,mongodb,docker,linux,git,githubactions" alt="Rust, TypeScript, Solidity, PostgreSQL, Redis, MongoDB, Docker, Linux, Git, and GitHub Actions" />
</p>

## What I am building now

```text
Tidebook                         Native Rust matching engine
   │                                         │
   ├─ finalized event ingestion              ├─ sequenced runtime
   ├─ indexed market state                   ├─ API integration
   ├─ query API                              ├─ persistence and replay
   └─ live order-book views                  └─ latency benchmarks
```

The two tracks study the same problem from different constraints: Tidebook must fit Solana's account and transaction model, while the native engine can optimize an in-memory single-writer hot path.

## Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kunal171/kunal171/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kunal171/kunal171/output/github-contribution-grid-snake.svg" />
  <img alt="Animated GitHub contribution trail" src="https://raw.githubusercontent.com/kunal171/kunal171/output/github-contribution-grid-snake.svg" />
</picture>

<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,55:0e7490,100:0f172a&height=110&section=footer"
    width="100%"
    alt="Footer"
  />
</p>
