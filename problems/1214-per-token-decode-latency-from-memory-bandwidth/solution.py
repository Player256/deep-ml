def estimate_decode_latency(num_params, bytes_per_param, bandwidth_bytes_per_s):
    total_space = num_params*bytes_per_param
    per_token_latency = (total_space / bandwidth_bytes_per_s) * 1000

    if per_token_latency > 1000:
        per_token_latency = per_token_latency / 1000
    
    tokens_per_sec = 1000 / per_token_latency

    return [per_token_latency, tokens_per_sec]
