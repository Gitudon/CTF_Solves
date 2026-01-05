require 'prime'

# 暗号化された文字列
encrypted_string = "Coufhlj@bixm|UF\\JCjP^P<"

# 暗号化された文字列をバイト配列に変換
encrypted_bytes = encrypted_string.bytes

# 最初の23個の素数を取得
primes = Prime::Generator23.new.take(23)

# XOR演算を逆に適用して元の入力バイトを復元
original_bytes = encrypted_bytes.zip(primes).map { |enc_byte, prime| enc_byte ^ prime }

# 復元したバイト配列を文字列に変換
flag = original_bytes.pack("C*")

puts "Flag: #{flag}"
