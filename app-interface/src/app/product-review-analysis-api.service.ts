import { Injectable, signal, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, finalize } from 'rxjs/operators';
import { of } from 'rxjs';

export interface AnalysisItem {
  aspect: string;
  sentiment: string;
}

export interface AnalysisResponse {
  review_text: string;
  analysis: AnalysisItem[];
}

@Injectable({
  providedIn: 'root'
})
export class ProductReviewAnalysisApiService {
  private readonly http = inject(HttpClient);

  // States managed by Signals
  readonly results = signal<AnalysisItem[]>([]);
  readonly loading = signal<boolean>(false);
  readonly serverOffline = signal<boolean>(false);
  readonly currentReviewText = signal<string>('');

  analyzeReview(reviewText: string): void {
    this.loading.set(true);
    this.serverOffline.set(false);
    this.results.set([]);
    this.currentReviewText.set(reviewText);

    this.http.post<AnalysisResponse>('/api/analyze', { review_text: reviewText })
      .pipe(
        catchError((error) => {
          console.error('API connection failed:', error);
          this.serverOffline.set(true);
          return of(null);
        }),
        finalize(() => {
          this.loading.set(false);
        })
      )
      .subscribe((response) => {
        if (response && response.analysis) {
          this.results.set(response.analysis);
        }
      });
  }
}
