# VTuber IRL Tracker

A real-time face-tracking pipeline that lets VTubers stream IRL while keeping their real identity hidden. Built using MediaPipe for facial landmark detection and Unity for real-time 3D avatar rendering — no camera passthrough required.

## Pipeline

```
Video input → MediaPipe (Python) → JSON → Unity (UniVRM) → Animated 3D avatar
```

1. **Tracking (Python + MediaPipe)** — Processes video frame-by-frame using MediaPipe's Face Landmarker, extracting 52 ARKit-style facial blendshapes and 3D head transform matrices.
2. **Data bridge (JSON)** — Tracking output is serialized into a structured per-frame schema, decoupling the tracking pipeline from the rendering engine.
3. **Rendering (Unity + UniVRM)** — Deserializes tracking data and drives a rigged VRM avatar in real time: blendshape weights mapped from ARKit to the avatar's native facial shapes, head rotation applied via bone transforms, and exponential smoothing to eliminate frame-to-frame jitter.

## Highlights

- Cross-language, decoupled architecture — Python tracking and Unity rendering communicate through a versioned data contract, allowing either half to be swapped or upgraded independently (e.g. offline video today, live webcam streaming later).
- Custom blendshape retargeting layer translating industry-standard ARKit facial coefficients to VRM's native shape-key system.
- Temporal smoothing applied to reduce landmark noise inherent to monocular tracking.

## Roadmap

- Live webcam capture for real-time streaming
- Full-body pose tracking (MediaPipe Pose Landmarker)
- Occlusion-robust tracking for hands-heavy activities (e.g. piano, hardware assembly)
