# Topic inventory

The old 265 one-rule files are **titles only**. Bodies were a style-guide dump; new skills rewrite examples. Every ID has one owning skill. Do not resurrect a file because it is listed here.

**Loadable skills** are only the keys in `directory.json` (files on disk). Names below that are not in `directory.json` are **not written** — do not route to them.

## Not written (planned skill ids)

When a skill is written, add `skills/<name>/SKILL.md` plus entries in `directory.json`, `skills.sh.json`, and the router.

| Planned id | Intended path |
|------------|---------------|
| `iterator-pipelines` | `skills/iterator-pipelines/` |
| `result-combinators` | `skills/result-combinators/` |
| `closures-and-hof` | `skills/closures-and-hof/` |
| `tokio-essentials` | `skills/tokio-essentials/` |
| `async-concurrency` | `skills/async-concurrency/` |
| `rayon-and-threads` | `skills/rayon-and-threads/` |
| `unsafe-essentials` | `skills/unsafe-essentials/` |
| `public-api-design` | `skills/public-api-design/` |
| `conversions-and-traits` | `skills/conversions-and-traits/` |
| `serde-essentials` | `skills/serde-essentials/` |
| `macros-essentials` | `skills/macros-essentials/` |
| `testing-essentials` | `skills/testing-essentials/` |
| `property-based-testing` | `skills/property-based-testing/` |
| `async-testing` | `skills/async-testing/` |
| `rustdoc-essentials` | `skills/rustdoc-essentials/` |
| `tracing-essentials` | `skills/tracing-essentials/` |
| `cargo-workspace` | `skills/cargo-workspace/` |
| `allocation-discipline` | `skills/allocation-discipline/` |
| `performance-tuning` | `skills/performance-tuning/` |
| `clippy-fmt` | `skills/clippy-fmt/` |
| `code-review` | `skills/code-review/` |
| `security-essentials` | `skills/security-essentials/` |
| `clap-cli` | `skills/clap-cli/` |
| `bug-fix` | `skills/bug-fix/` |
| `quality` | `skills/quality/` |
| `code-review-playbook` | `skills/code-review-playbook/` |
| `setup` | `skills/setup/` |
| `new-crate` | `skills/new-crate/` |
| `unsafe-change` | `skills/unsafe-change/` |

## rust-essentials

`name-types-camel` `name-variants-camel` `name-funcs-snake` `name-consts-screaming` `name-lifetime-short` `name-type-param-single` `name-as-free` `name-to-expensive` `name-into-ownership` `name-no-get-prefix` `name-is-has-bool` `name-iter-convention` `name-iter-method` `name-iter-type-match` `name-acronym-word` `name-crate-no-rs`

`pat-let-else` `pat-matches-macro` `pat-if-let-chains` `pat-exhaustive-enum` `pat-at-bindings`

`type-display-vs-debug` `type-numeric-fmt`

`coll-binaryheap` `coll-map-choice` `coll-seq-choice` `coll-set-membership`

`anti-over-abstraction`

## ownership-borrowing

`own-borrow-over-clone` `own-slice-over-vec` `own-cow-conditional` `own-arc-shared` `own-rc-single-thread` `own-refcell-interior` `own-mutex-interior` `own-rwlock-readers` `own-copy-small` `own-clone-explicit` `own-move-large` `own-lifetime-elision`

`anti-clone-excessive` `anti-string-for-str` `anti-vec-for-slice`

## type-driven-design

`type-newtype-ids` `type-newtype-validated` `type-enum-states` `type-option-nullable` `type-result-fallible` `type-phantom-marker` `type-never-diverge` `type-generic-bounds` `type-no-stringly` `type-repr-transparent` `type-deref-coercion`

`api-newtype-safety` `api-typestate` `api-parse-dont-validate`

`const-block` `const-fn` `const-generics` `const-vs-static`

`num-overflow-explicit` `num-cast-try-from` `num-float-compare` `num-saturating-clamp` `num-nonzero`

`anti-stringly-typed`

## error-handling

`err-thiserror-lib` `err-anyhow-app` `err-result-over-panic` `err-context-chain` `err-no-unwrap-prod` `err-expect-bugs-only` `err-question-mark` `err-from-impl` `err-source-chain` `err-lowercase-msg` `err-doc-errors` `err-custom-type`

`anti-unwrap-abuse` `anti-expect-lazy` `anti-empty-catch` `anti-panic-expected`

## iterator-pipelines

`perf-iter-over-index` `perf-iter-lazy` `perf-collect-once` `perf-collect-into` `perf-chain-avoid` `anti-index-over-iter` `anti-collect-intermediate`

## result-combinators

No unique old IDs. `err-question-mark` stays in `error-handling`. This skill owns `Option`/`Result` combinators (`map`, `and_then`, `map_err`) as the FP railway.

## closures-and-hof

`closure-fn-trait-bounds` `closure-impl-fn-return` `closure-move-capture` `closure-static-vs-dyn` `closure-disjoint-capture`

## tokio-essentials

`async-tokio-runtime` `async-spawn-blocking` `async-tokio-fs` `async-fn-in-trait` `async-async-fn-bounds` `async-cancellation-token` `async-cancel-safety` `async-clone-before-await`

## async-concurrency

`async-no-lock-await` `async-join-parallel` `async-try-join` `async-select-racing` `async-bounded-channel` `async-mpsc-queue` `async-broadcast-pubsub` `async-watch-latest` `async-oneshot-response` `async-joinset-structured`

`anti-lock-across-await`

## rayon-and-threads

`conc-rayon-par-iter` `conc-scoped-threads` `conc-atomic-ordering` `conc-thread-local`

## unsafe-essentials

`unsafe-safety-comment` `unsafe-minimize-scope` `unsafe-miri-ci` `unsafe-maybeuninit` `unsafe-extern-block` `unsafe-send-sync-manual` `unsafe-no-mangle-unsafe`

## public-api-design

`api-builder-pattern` `api-builder-must-use` `api-sealed-trait` `api-extension-trait` `api-impl-into` `api-impl-asref` `api-must-use` `api-non-exhaustive` `api-from-not-into` `api-default-impl` `api-common-traits` `api-serde-optional` `api-impl-fromiterator` `api-operator-overload`

## conversions-and-traits

`conv-tryfrom-fallible` `conv-fromstr-parsing` `conv-asmut-mutable`

`trait-associated-type-vs-generic` `trait-blanket-impl` `trait-coherence-newtype` `trait-default-methods` `trait-dyn-vs-generic` `trait-object-safety`

`anti-type-erasure`

## serde-essentials

`serde-rename-all` `serde-default-compat` `serde-skip-empty` `serde-flatten` `serde-enum-representation` `serde-deny-unknown-fields` `serde-custom-with` `serde-try-from-validate`

## macros-essentials

`macro-prefer-functions` `macro-rules-hygiene` `macro-fragment-specifiers` `macro-export-crate-path` `macro-private-helpers` `macro-proc-two-crate` `macro-proc-syn-quote` `macro-proc-error-spans`

## testing-essentials

`test-cfg-test-module` `test-use-super` `test-integration-dir` `test-descriptive-names` `test-arrange-act-assert` `test-mockall-mocking` `test-mock-traits` `test-fixture-raii` `test-should-panic` `test-doctest-examples` `test-snapshot-testing` `test-loom-concurrency`

## property-based-testing

`test-proptest-properties`

## async-testing

`test-tokio-async`

## rustdoc-essentials

`doc-all-public` `doc-module-inner` `doc-examples-section` `doc-errors-section` `doc-panics-section` `doc-safety-section` `doc-question-mark` `doc-hidden-setup` `doc-intra-links` `doc-link-types` `doc-cargo-metadata` `doc-crate-readme`

## tracing-essentials

`obs-tracing-over-log` `obs-library-facade` `obs-structured-fields` `obs-instrument-spans` `obs-levels-filter` `obs-error-chain`

## security-essentials

`obs-no-sensitive-data`

## cargo-workspace

`proj-lib-main-split` `proj-mod-by-feature` `proj-flat-small` `proj-mod-rs-dir` `proj-pub-crate-internal` `proj-pub-super-parent` `proj-pub-use-reexport` `proj-prelude-module` `proj-bin-dir` `proj-workspace-large` `proj-workspace-deps` `proj-feature-additive` `proj-msrv-declare` `proj-build-rs-minimal`

## allocation-discipline

`mem-with-capacity` `mem-smallvec` `mem-arrayvec` `mem-box-large-variant` `mem-boxed-slice` `mem-thinvec` `mem-clone-from` `mem-reuse-collections` `mem-avoid-format` `mem-write-over-format` `mem-arena-allocator` `mem-zero-copy` `mem-compact-string` `mem-smaller-integers` `mem-assert-type-size` `mem-take-replace` `mem-drop-order`

`perf-drain-reuse` `perf-extend-batch` `perf-entry-api` `anti-format-hot-path`

Ponytail: `Vec` / `std` first. SmallVec, ThinVec, arenas only after a measurement.

## performance-tuning

`opt-inline-small` `opt-inline-always-rare` `opt-inline-never-cold` `opt-cold-unlikely` `opt-likely-hint` `opt-lto-release` `opt-codegen-units` `opt-pgo-profile` `opt-target-cpu` `opt-bounds-check` `opt-simd-portable` `opt-cache-friendly`

`perf-profile-first` `perf-release-profile` `perf-black-box-bench` `perf-ahash` `perf-io-buffering` `test-criterion-bench`

`anti-premature-optimize`

## clippy-fmt

`lint-deny-correctness` `lint-warn-suspicious` `lint-warn-style` `lint-warn-complexity` `lint-warn-perf` `lint-pedantic-selective` `lint-missing-docs` `lint-unsafe-doc` `lint-cargo-metadata` `lint-rustfmt-check` `lint-workspace-lints` `lint-cfg-check` `lint-clippy-nursery-selected`

## New (no old ID)

Written: `load-context`, `tdd`, `rust-skill-router`. Planned: see **Not written** above (`clap-cli` and remaining playbooks).
