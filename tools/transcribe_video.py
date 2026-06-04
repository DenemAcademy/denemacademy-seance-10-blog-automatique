from __future__ import annotations

import json
import sys
from pathlib import Path

from faster_whisper import WhisperModel


ROOT = Path(__file__).resolve().parents[1]


def fmt(seconds: float) -> str:
    total = int(seconds)
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def main() -> int:
    source = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "0601.mp4")
    if not source.exists():
        raise FileNotFoundError(source)

    out_dir = ROOT / "transcription"
    out_dir.mkdir(exist_ok=True)
    jsonl_path = out_dir / "seance-10-segments.jsonl"
    json_path = out_dir / "seance-10-segments.json"
    raw_path = out_dir / "seance-10-transcription-brute.txt"

    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(source),
        language="fr",
        vad_filter=True,
        beam_size=5,
        word_timestamps=False,
    )

    collected: list[dict[str, object]] = []
    with jsonl_path.open("w", encoding="utf-8") as jf, raw_path.open("w", encoding="utf-8") as tf:
        tf.write(f"Source: {source.name}\n")
        tf.write(f"Langue: {info.language} ({info.language_probability:.2f})\n\n")
        for idx, seg in enumerate(segments, 1):
            item = {
                "id": idx,
                "start": round(seg.start, 2),
                "end": round(seg.end, 2),
                "start_hms": fmt(seg.start),
                "end_hms": fmt(seg.end),
                "text": seg.text.strip(),
            }
            collected.append(item)
            jf.write(json.dumps(item, ensure_ascii=False) + "\n")
            jf.flush()
            tf.write(f"[{item['start_hms']} - {item['end_hms']}] {item['text']}\n")
            tf.flush()
            if idx % 50 == 0:
                print(f"{idx} segments transcrits, dernier timestamp {item['end_hms']}", flush=True)

    json_path.write_text(json.dumps(collected, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Transcription terminee: {len(collected)} segments", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
