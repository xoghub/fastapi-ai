import { Component, ChangeDetectionStrategy, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { ProductReviewAnalysisApiService } from './product-review-analysis-api.service';

@Component({
  selector: 'app-product-review-analysis',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './product-review-analysis.html',
  styleUrl: './product-review-analysis.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProductReviewAnalysisComponent {
  private readonly fb = inject(FormBuilder);
  readonly apiService = inject(ProductReviewAnalysisApiService);

  // Reactive form for review text input
  readonly reviewForm = this.fb.group({
    reviewText: ['', [Validators.required, Validators.minLength(10), Validators.maxLength(500)]]
  });

  get reviewTextControl() {
    return this.reviewForm.get('reviewText');
  }

  onSubmit(): void {
    if (this.reviewForm.invalid) {
      return;
    }

    const reviewText = this.reviewForm.value.reviewText;
    if (reviewText) {
      this.apiService.analyzeReview(reviewText.trim());
    }
  }

  // Clear helper
  onClear(): void {
    this.reviewForm.reset({ reviewText: '' });
  }
}
