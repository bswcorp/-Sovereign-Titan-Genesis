# SOVEREIGN SELECTION ALGORITHM (SSA) v1.0
# Objective: Identify the Top 5 Heirs for the QDMS Protocol

import json

def calculate_council():
    try:
        with open("../database/guardian_metrics.json", "r") as f:
            candidates = json.load(f)
    except FileNotFoundError:
        print("🚨 Data metrics not found. Tournament delayed.")
        return

    scored_candidates = []

    for c in candidates:
        # L: Logic (Bugs found)
        # F: Fortitude (Uptime/Syncs)
        # T: Time (Badge seniority)
        l_score = c['bugs_found'] * 100
        f_score = c['sync_count'] * 10
        t_multiplier = 1.5 if c['is_first_1000'] else 1.0
        
        total_score = (l_score + f_score) * t_multiplier
        scored_candidates.append({
            "address": c['address'],
            "score": total_score
        })

    # Sort by highest score
    scored_candidates.sort(key=lambda x: x['score'], reverse=True)

    council_of_five = scored_candidates[:5]

    print("-" * 60)
    print("🏆 THE COUNCIL OF FIVE - CURRENT STANDINGS")
    print("-" * 60)
    for i, member in enumerate(council_of_five):
        print(f"RANK {i+1}: {member['address']} | SCORE: {member['score']}")
    print("-" * 60)
    print("📜 STATUS: PENDING FINAL ARSITEK VETO")

if __name__ == "__main__":
    calculate_council()
  
