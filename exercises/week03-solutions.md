# Week 3: break the cipher on paper

Work one exercise at a time. Read the idea, follow the calculation, then try the short check without looking back.

The week 3 sheet assigns **3.1, 3.3, 3.5, 3.6, and 3.8**. The questions were checked visually on printed pages 42–43, PDF page 23, of Lars Ramkilde Knudsen's *Cryptology - how to crack it*, first edition, 2018. The local filename is `cryptology_essence.pdf`; the course calls its text *Cryptology in Essence*. Equivalence between editions is unconfirmed. These solutions use the actual questions in the local scan, plus the four hints in `week03.pdf`.

## The symbols you need

- $m$ is a plaintext block, the message before encryption.
- $c$ is a ciphertext block, the encrypted message.
- $E_k$ encrypts with key $k$. $D_k$ undoes that encryption.
- $\bar x$ flips every bit. For example, $\overline{1010}=0101$.
- $\oplus$ is XOR. Equal bits give 0; different bits give 1.

The useful XOR trick is $x\oplus y\oplus y=x$. XOR the same value twice and it cancels.

## Exercise 3.1: test two DES keys for the price of one

**Goal.** Use the DES complementation property to search half the key space.

The property is

$$E_{\bar k}(\bar m)=\overline{E_k(m)}.$$

It flips the **key, message, and output together**.

### Step 1. Ask for two ciphertexts

Choose one 64-bit message $m$. Ask for its encryption and the encryption of its complement under the secret key $k$:

$$c=E_k(m),\qquad c'=E_k(\bar m).$$

This is a chosen-plaintext attack because we choose these two inputs.

### Step 2. Group the keys into pairs

DES has $2^{56}$ effective keys. Pair each candidate $a$ with $\bar a$.

No bit string equals its own complement. Every key belongs to exactly one pair, so there are

$$\frac{2^{56}}2=2^{55}\text{ pairs}.$$

For example, choose the representative whose first effective key bit is 0. Its complement starts with 1.

### Step 3. Encrypt once, then make two comparisons

For each representative $a$, compute just

$$t=E_a(m).$$

Use that one result in both tests:

| Test | What it tells us |
|---|---|
| $t=c$ | $a$ is a candidate for the secret key. |
| $t=\bar c'$ | $\bar a$ is a candidate for the secret key. |

Why does the second test work? If the secret key is $\bar a$, then

$$c'=E_{\bar a}(\bar m)=\overline{E_a(m)}=\bar t.$$

Therefore $t=\bar c'$. One DES evaluation has tested both members of the pair against known data.

A match is a **candidate**, not a proof. Check that key against both supplied pairs. If an accidental match survives, use another plaintext/ciphertext pair.

### Step 4. Count the work consistently

| Search | Worst-case main search | Average main search for a uniformly placed key |
|---|---|---|
| Ordinary exhaustive search | $2^{56}$ DES evaluations | About $2^{55}$ |
| Complement-pair search | $2^{55}$ DES evaluations | About $2^{54}$ |

Candidate checks add a small extra cost. The main search is twice as fast. It is still exponential and still written $O(2^{56})$ if we ignore constant factors.

**Answer.** Query $m$ and $\bar m$, examine one representative per key pair, and compare each result with $c$ and $\bar c'$. The main search needs at most $2^{55}$ encryptions.

**Try it.** If a toy cipher had 8-bit keys and the same property, how many pairs would there be? **Check:** $2^7=128$.

## Exercise 3.3: equal CBC ciphertext blocks leak a relationship

**Goal.** Find what an observer learns when $c_i=c_j$ for different positions.

CBC encryption is

$$c_i=E_k(m_i\oplus c_{i-1}),$$

where $c_0$ is the initialization vector, or IV.

### Step 1. Equal outputs mean equal inputs

For a fixed key, a block cipher is invertible. So if $c_i=c_j$, then

$$m_i\oplus c_{i-1}=m_j\oplus c_{j-1}.$$

### Step 2. Cancel the terms we do not want

XOR both sides with $m_j\oplus c_{i-1}$:

$$\boxed{m_i\oplus m_j=c_{i-1}\oplus c_{j-1}.}$$

The observer can calculate the right-hand side from the preceding ciphertext blocks. If a position is the first block, the relevant preceding value is the IV, which must be known for that calculation.

### Step 3. See what this reveals

Suppose the preceding blocks are `1010` and `1100`. Their XOR is `0110`.

The observer now knows $m_i\oplus m_j=0110$. If they also know $m_i=0011$, then

```text
m_j = 0011 XOR 0110 = 0101
```

**Answer.** Equal ciphertext blocks reveal the XOR of two plaintext blocks. Knowing either plaintext block reveals the other. Equal ciphertext blocks alone do **not** imply equal plaintext blocks.

**Try it.** When would the two plaintext blocks be equal? **Check:** when the preceding ciphertext blocks are also equal.

## Exercise 3.5: how many known blocks identify a key?

**Goal.** Work out how many distinct plaintext/ciphertext pairs usually leave only the actual key.

### Step 1. Count the wrong keys that survive

Let the key length be $\ell$ bits and the block length be $b$ bits.

A wrong key passes one random block test with probability about $2^{-b}$. Under the exercise's independence approximation, it passes $t$ distinct block tests with probability about $2^{-bt}$.

There are $2^\ell-1$ wrong keys. Their expected surviving count is

$$\lambda=(2^\ell-1)2^{-bt}\approx2^{\ell-bt}.$$

We want $\lambda$ much smaller than 1. Repeating the **same** pair gives no new information.

### Step 2. Try DES

DES has a 56-bit effective key and 64-bit blocks. One pair gives

$$\lambda\approx2^{56-64}=2^{-8}=\frac1{256}.$$

So one pair usually identifies the key. By the union bound, the probability of any wrong match is at most about $1/256$. The chance of no wrong match is at least about **99.6%** under this model.

### Step 3. Apply the same subtraction to each cipher

| Cipher | Key bits $\ell$ | Block bits $b$ | Known pairs $t$ | Expected wrong keys $\lambda$ |
|---|---:|---:|---:|---:|
| DES | 56 | 64 | **1** | $2^{-8}$ |
| Two-key Triple-DES | 112 | 64 | **2** | $2^{-16}$ |
| Three-key Triple-DES | 168 | 64 | **3** | $2^{-24}$ |
| AES-128 | 128 | 128 | **2** | $2^{-128}$ |
| AES-192 | 192 | 128 | **2** | $2^{-64}$ |
| AES-256 | 256 | 128 | **3** | $2^{-128}$ |

The AES block size is always 128 bits. Only the key length changes. These sizes follow [NIST FIPS 197](https://csrc.nist.gov/pubs/fips/197/final). The DES and Triple-DES key sizes follow the historical [NIST DES standard](https://csrc.nist.gov/pubs/fips/46-3/final). We count effective key bits, excluding DES parity bits.

### Step 4. Avoid the “expected one” trap

For AES-128 with one pair, $2^{128-128}=1$. That means about **one wrong key**, in addition to the true key.

Under the independent random-key model, the probability that no wrong key survives is approximately $e^{-\lambda}$. When $\lambda=1$, that is about 37%, which is not a high chance of uniqueness.

AES-256 with two pairs has the same problem. A third pair removes almost all accidental candidates.

**Answer.** DES needs 1 pair; the two Triple-DES variants need 2 and 3; AES-128, AES-192, and AES-256 need 2, 2, and 3 respectively, for high-confidence uniqueness under the stated approximation.

The phrase “good probability” has no numerical threshold in the question. The counts above use the usual requirement that expected wrong matches be far below 1. They are counts for distinguishing keys, not estimates of practical attack strength.

**Try it.** A toy cipher has 20-bit keys and 8-bit blocks. Two pairs leave about 16 wrong keys. Three leave about $1/16$. A fourth leaves about $1/4096$.

## Exercise 3.6: meet in the middle of double-DES

**Goal.** Explain why two DES encryptions do not give a $2^{112}$-work key search.

Double-DES uses two 56-bit keys:

$$c=E_{k_2}(E_{k_1}(m)).$$

### Step 1. Undo the outer encryption

Apply $D_{k_2}$ to both sides:

$$\boxed{E_{k_1}(m)=D_{k_2}(c).}$$

The encryption from the left and decryption from the right must meet at the same intermediate block. This holds for both given pairs $(m_1,c_1)$ and $(m_2,c_2)$.

### Step 2. Count accidental matches with one pair

There are $2^{56}\cdot2^{56}=2^{112}$ possible key pairs. Two random 64-bit intermediate blocks agree with probability about $2^{-64}$.

So one known pair leaves roughly

$$2^{112}\cdot2^{-64}=2^{48}$$

matching key pairs. That is far too many to identify the key.

### Step 3. Use the second known pair

A wrong key pair must now pass two 64-bit checks. The expected number of wrong survivors is approximately

$$2^{112}\cdot2^{-128}=2^{-16}.$$

The actual key pair always survives. The expected **total** is therefore approximately $1+2^{-16}$, usually just the actual pair. This is the precise meaning of the book's rounded statement “one”.

### Step 4. Build the two lists requested in the question

For every possible 56-bit key $a$, put this record in $L_1$:

$$(E_a(m_1),E_a(m_2),a).$$

For every possible 56-bit key $b$, put this record in $L_2$:

$$(D_b(c_1),D_b(c_2),b).$$

Each list has $2^{56}$ records.

### Step 5. Match the first two fields

1. Sort both lists by their first two fields, treated as a pair.
2. Walk through the sorted lists, comparing those pairs of fields.
3. If the fields match, the key from $L_1$ is a candidate $k_1$ and the key from $L_2$ is a candidate $k_2$.
4. Keep every candidate if several records match. Verify candidates by double-encrypting the known messages. Use an extra known pair if ambiguity remains.

The correct key pair must appear because Step 1 proves both intermediate values match.

### Step 6. Count the cost

Building the two lists uses $4\cdot2^{56}=2^{58}$ single-DES evaluations, since each record contains two computed blocks. That is $O(2^{56})$ cipher work when constants are omitted.

Comparison sorting adds $O(2^{56}\log_2 2^{56})$ comparisons. Matching sorted lists is linear, apart from processing duplicate groups. Storage is $O(2^{56})$ records, which is enormous.

A hash-table version has expected $O(2^{56})$ lookup work but still needs enormous storage. Either approach is far below trying all $2^{112}$ key pairs one by one.

**Answer.** Match $E_{k_1}(m)$ with $D_{k_2}(c)$. Two known pairs usually identify the actual pair, and the main cipher work has exponent 56 rather than 112.

**Try it.** With 8-bit keys, how large is each list? **Check:** 256 records, versus 65,536 possible key pairs.

## Exercise 3.8: undo encryption with two feedback values

**Goal.** Decrypt the mode

$$c_i=E_k(m_i\oplus c_{i-1})\oplus m_{i-1},$$

where $m_0$ and $c_0$ are the initial values.

### Step 1. Remove the XOR outside the cipher

XOR both sides with $m_{i-1}$:

$$c_i\oplus m_{i-1}=E_k(m_i\oplus c_{i-1}).$$

### Step 2. Undo the encryption

Apply $D_k$:

$$D_k(c_i\oplus m_{i-1})=m_i\oplus c_{i-1}.$$

### Step 3. Remove the remaining XOR

XOR both sides with $c_{i-1}$:

$$\boxed{m_i=D_k(c_i\oplus m_{i-1})\oplus c_{i-1}.}$$

To recover $m_1$, use the agreed $m_0$ and $c_0$. Then use the recovered $m_1$ to recover $m_2$, and continue.

### A four-bit example

Use a deliberately insecure toy cipher $E(x)=(x+3)\bmod16$. Its inverse is $D(x)=(x-3)\bmod16$.

Let $m_0=0$, $c_0=5$, and $m_1=9$.

1. $m_1\oplus c_0=9\oplus5=12$.
2. $E(12)=15$.
3. $c_1=15\oplus0=15$.
4. Decrypt with $D(15\oplus0)\oplus5=12\oplus5=9$.

We recover the original message block.

### Compare with CBC

| Property | CBC | This exercise's mode |
|---|---|---|
| Encryption | $E_k(m_i\oplus c_{i-1})$ | $E_k(m_i\oplus c_{i-1})\oplus m_{i-1}$ |
| Decryption | $D_k(c_i)\oplus c_{i-1}$ | $D_k(c_i\oplus m_{i-1})\oplus c_{i-1}$ |
| Initial values | $c_0$ | $c_0$ and $m_0$ |
| Encrypt blocks in parallel? | No, each needs the previous ciphertext. | No, each needs the previous ciphertext. |
| Decrypt blocks in parallel? | Yes, given the ciphertext and IV. | Normally no, each needs the recovered previous plaintext. |
| One corrupted ciphertext block | Corrupts the corresponding plaintext block; flips corresponding bits in the next; later blocks recover. | Generally keeps propagating through the recovered plaintext feedback. There is no guaranteed recovery after two blocks. |

For the final row, a wrong $m_i$ becomes an input to the next decryption. That wrong result then becomes an input to the following decryption. Special cancellations can occur; continued corruption is not a proof that every later block must differ in every case.

Equal ciphertext blocks also no longer give the direct CBC relation from Exercise 3.3, because the block-cipher inputs during decryption contain different preceding plaintext blocks.

**Answer.** Decrypt with $D_k(c_i\oplus m_{i-1})\oplus c_{i-1}$. Compared with CBC, plaintext feedback makes decryption sequential and generally extends error propagation. Neither formula alone authenticates the message.

**Try it.** Continue the toy example with $m_2=6$. **Check:** $c_2=5$, and $D(5\oplus9)\oplus15=6$.

## Implementation: try AES with fewer rounds

The week 3 implementation is AES-128 with a selectable 2–10 rounds. Start with the runnable examples and state diagrams in [the AES walkthrough](../docs/aes-walkthrough.md). The code lives in [aes.py](../crypto_library/aes.py).

## Check the small numerical examples yourself

Run this from the repository root with Python 3.9 or newer. It checks the displayed arithmetic and exhaustively checks the Exercise 3.8 inverse for every four-bit input and feedback combination. It does not replace the general algebraic proofs above.

```bash
python3 - <<'PY'
assert 2**56 // 2 == 2**55
assert 0b1010 ^ 0b1100 == 0b0110
assert 0b0011 ^ 0b0110 == 0b0101
for key_bits, block_bits, pairs, exponent in [
    (56, 64, 1, -8), (112, 64, 2, -16), (168, 64, 3, -24),
    (128, 128, 2, -128), (192, 128, 2, -64), (256, 128, 3, -128),
]:
    assert key_bits - block_bits * pairs == exponent
assert 112 - 64 == 48
assert 112 - 2 * 64 == -16
assert (((9 ^ 5) + 3) % 16) ^ 0 == 15
assert (((6 ^ 15) + 3) % 16) ^ 9 == 5
for message in range(16):
    for previous_message in range(16):
        for previous_ciphertext in range(16):
            ciphertext = ((message ^ previous_ciphertext) + 3) % 16
            ciphertext ^= previous_message
            recovered = ((ciphertext ^ previous_message) - 3) % 16
            recovered ^= previous_ciphertext
            assert recovered == message
print('Week 3 arithmetic passed; all 4096 toy decryptions recovered the message.')
PY
```
